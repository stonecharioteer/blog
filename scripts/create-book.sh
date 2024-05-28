#!/bin/bash

set -euo pipefail

# Check if gum is installed
if ! command -v gum &> /dev/null; then
    echo "Error: gum could not be found. Please install gum and try again." >&2
    exit 1
fi

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq could not be found. Please install jq and try again." >&2
    exit 1
fi

# Help function
show_help() {
    echo "Usage: $0 [options]"
    echo
    echo "Options:"
    echo "  -t, --title            Book title"
    echo "  -a, --author           Author name"
    echo "  -i, --image            Book image path"
    echo "  -s, --isbn             ISBN"
    echo "  -g, --tags             Tags (comma separated)"
    echo "  -d, --date             Date of purchase"
    echo "  -j, --json             JSON file with values"
    echo "  -h, --help             Display this help message"
    echo
    echo "If any option is omitted, you will be prompted to enter it."
}

# Initialize variables
BOOK_TITLE=""
AUTHOR_NAME=""
BOOK_IMAGE_PATH=""
ISBN=""
TAGS=""
DATE_OF_PURCHASE=""
JSON_FILE=""

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -t|--title) BOOK_TITLE="$2"; shift ;;
        -a|--author) AUTHOR_NAME="$2"; shift ;;
        -i|--image) BOOK_IMAGE_PATH="$2"; shift ;;
        -s|--isbn) ISBN="$2"; shift ;;
        -g|--tags) TAGS="$2"; shift ;;
        -d|--date) DATE_OF_PURCHASE="$2"; shift ;;
        -j|--json) JSON_FILE="$2"; shift ;;
        -h|--help) show_help; exit 0 ;;
        *) echo "Unknown parameter passed: $1" >&2; show_help; exit 1 ;;
    esac
    shift
done

# Load values from JSON file if provided
if [ -n "$JSON_FILE" ]; then
    if [ ! -f "$JSON_FILE" ]; then
        echo "Error: JSON file does not exist at path $JSON_FILE" >&2
        exit 3
    fi
    BOOK_TITLE=$(jq -r '.BOOK_TITLE' "$JSON_FILE")
    AUTHOR_NAME=$(jq -r '.AUTHOR_NAME' "$JSON_FILE")
    BOOK_IMAGE_PATH=$(jq -r '.BOOK_IMAGE_PATH' "$JSON_FILE")
    ISBN=$(jq -r '.ISBN' "$JSON_FILE")
    TAGS=$(jq -r '.TAGS' "$JSON_FILE")
    DATE_OF_PURCHASE=$(jq -r '.DATE_OF_PURCHASE' "$JSON_FILE")
fi

# Prompt for input using gum if arguments are not provided, offering default values from JSON
if [ -z "$BOOK_TITLE" ];then
    BOOK_TITLE=$(gum input --placeholder "Book Title" --value "$BOOK_TITLE")
fi
if [ -z "$AUTHOR_NAME" ];then
    AUTHOR_NAME=$(gum input --placeholder "Author Name" --value "$AUTHOR_NAME")
fi
if [ -z "$BOOK_IMAGE_PATH" ];then
    BOOK_IMAGE_PATH=$(gum input --placeholder "Book Image Path" --value "$BOOK_IMAGE_PATH")
    if [ ! -f "$BOOK_IMAGE_PATH" ];then
        echo "Error: Image file does not exist at path $BOOK_IMAGE_PATH" >&2
        exit 2
    fi
fi
if [ -z "$ISBN" ];then
    ISBN=$(gum input --placeholder "ISBN" --value "$ISBN")
fi
if [ -z "$TAGS" ];then
    TAGS=$(gum input --placeholder "Tags (comma separated)" --value "$TAGS")
fi
if [ -z "$DATE_OF_PURCHASE" ];then
    DATE_OF_PURCHASE=$(gum input --placeholder "Date of Purchase" --value "$DATE_OF_PURCHASE")
fi

# Convert author name from "Firstname Lastname" to "Lastname-Firstname"
if [ -n "$AUTHOR_NAME" ];then
    AUTHOR_NAME_FILENAME=$(echo "$AUTHOR_NAME" | awk '{print $2"-"$1}' | tr -d ' ')
fi

# Create the new file path
BOOK_TITLE_FILENAME=$(echo "$BOOK_TITLE" | tr ' ' '-')
FILE_PATH="./source/reading/catalogue/books/${AUTHOR_NAME_FILENAME}--${BOOK_TITLE_FILENAME}.rst"
JSON_OUTPUT="./${AUTHOR_NAME_FILENAME}--${BOOK_TITLE_FILENAME}.json"

# Get the image extension and create the new image path
IMAGE_EXTENSION="${BOOK_IMAGE_PATH##*.}"
NEW_IMAGE_PATH="./source/_static/images/catalogue/books/${AUTHOR_NAME_FILENAME}--${BOOK_TITLE_FILENAME}.${IMAGE_EXTENSION}"

# Output the new values and paths
echo "Book Title: $BOOK_TITLE"
echo "Author Name: $AUTHOR_NAME"
echo "Book Image Path: $(realpath "$BOOK_IMAGE_PATH")"
echo "ISBN: $ISBN"
echo "Tags: $TAGS"
echo "Date of Purchase: $DATE_OF_PURCHASE"
echo "New Book File Path: $(realpath "$FILE_PATH")"
echo "New Image Path: $(realpath "$NEW_IMAGE_PATH")"

# Confirm whether to proceed
if ! gum confirm "Do you want to proceed with these values?";then
    echo "Operation cancelled."
    exit 0
fi

# Write raw input values to JSON file
cat <<EOF > "$JSON_OUTPUT"
{
    "BOOK_TITLE": "$BOOK_TITLE",
    "AUTHOR_NAME": "$AUTHOR_NAME",
    "BOOK_IMAGE_PATH": "$BOOK_IMAGE_PATH",
    "ISBN": "$ISBN",
    "TAGS": "$TAGS",
    "DATE_OF_PURCHASE": "$DATE_OF_PURCHASE"
}
EOF

# Copy the template file to the new file
cp ./source/reading/catalogue/books/new-book-template.rst $FILE_PATH

# Copy the image to the new path
cp "$BOOK_IMAGE_PATH" "$NEW_IMAGE_PATH"

# Replace the keywords in the new file
sed -i "s|{{BOOK_TITLE}}|$BOOK_TITLE|g" $FILE_PATH
sed -i "s|{{AUTHOR_NAME}}|$AUTHOR_NAME|g" $FILE_PATH
sed -i "s|{{BOOK_IMAGE_PATH}}|$NEW_IMAGE_PATH|g" $FILE_PATH
sed -i "s|{{ISBN}}|$ISBN|g" $FILE_PATH
sed -i "s|{{TAGS}}|$TAGS|g" $FILE_PATH
sed -i "s|{{DATE_OF_PURCHASE}}|$DATE_OF_PURCHASE|g" $FILE_PATH

echo "New book file created at $FILE_PATH"
echo "Image copied to $NEW_IMAGE_PATH"
echo "Values saved to JSON file at $JSON_OUTPUT"
