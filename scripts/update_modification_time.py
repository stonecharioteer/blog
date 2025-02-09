#!/usr/bin/env python3

import subprocess
import os
import re
from datetime import datetime

# List of files to ignore (relative paths)
IGNORE_FILES = {"source/resume/resume.rst", "README.rst"}

def get_tracked_rst_files():
    """Returns a list of all tracked .rst files in the repo."""
    result = subprocess.run(["git", "ls-files", "*.rst"], capture_output=True, text=True)
    return [file.strip() for file in result.stdout.splitlines() if file.strip() and file.strip() not in IGNORE_FILES]

def get_last_modified_date(file_path):
    """Returns the last commit modification date formatted as 'Apr 20, 2022'."""
    result = subprocess.run(["git", "log", "-1", "--format=%cd", "--date=format:%Y-%m-%d", "--", file_path], 
                            capture_output=True, text=True)
    date_str = result.stdout.strip()
    if date_str:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%b %d, %Y")  # Convert to 'Apr 20, 2022' format
    return None

def process_file(file_path):
    """Updates or inserts the modified_date variable in the file."""
    if not os.path.exists(file_path):
        return
    
    mod_date = get_last_modified_date(file_path)
    if not mod_date:
        return  # Skip files with no Git history

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated = False
    date_pattern = re.compile(r"^\.\. \|modified_date\| replace:: (.+)$")

    # Check if modified_date exists
    for i, line in enumerate(lines):
        match = date_pattern.match(line)
        if match:
            current_date = match.group(1)
            if current_date != mod_date:
                lines[i] = f".. |modified_date| replace:: {mod_date}\n"
                updated = True
            break
    else:
        # Append modified_date at the end if missing
        lines.append(f"\n.. |modified_date| replace:: {mod_date}\n")
        lines.append(".. note::\n    This file was last edited on |modified_date|\n")
        updated = True

    if updated:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"Updated: {file_path}")

def main():
    files = get_tracked_rst_files()
    for file in files:
        process_file(file)
    print("All tracked .rst files checked. Only modified files were updated.")

if __name__ == "__main__":
    main()
