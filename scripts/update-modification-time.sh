#!/usr/bin/env bash

# Enable strict mode for better error handling
set -euo pipefail

# Find all .rst files in the repository
FILES=$(find . -type f -name "*.rst")

for file in $FILES; do
    if [[ -f "$file" ]]; then
        # Get last commit modification date
        MOD_DATE=$(git log -1 --format="%cd" --date=format:'%Y-%m-%d' -- "$file" 2>/dev/null || true)

        # If the file is not tracked by Git, use the current date
        if [[ -z "$MOD_DATE" ]]; then
            MOD_DATE=$(date +"%Y-%m-%d")
        fi

        # Check if file already contains "|modified_date|" variable
        if grep -q '^\.\. \|modified_date\| replace::' "$file"; then
            # Update the existing modified_date variable (using # as delimiter)
            sed -i "s#^\.\. |modified_date| replace:: .*#.. |modified_date| replace:: $MOD_DATE#" "$file"
        else
            # Append the modified_date variable and ".. note::" at the end if missing
            echo -e "\n.. |modified_date| replace:: $MOD_DATE" >> "$file"
            echo -e "\n.. note::\n    This file was last edited on |modified_date|" >> "$file"
        fi

        # Log the processed file path
        echo "Updated: $file"
    fi
done

echo "All .rst files updated successfully."
