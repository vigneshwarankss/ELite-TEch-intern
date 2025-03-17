# ELite-TEch-intern
File Integrity Checker

Description

The File Integrity Checker is a Python tool that monitors changes in files by calculating and comparing their hash values. It helps detect modifications, additions, or deletions of files in a specified directory, ensuring file integrity.

Features

✅ Compute and store SHA-256 hash values of files
✅ Detect modified, added, and deleted files
✅ Save hash records in a JSON file
✅ Scan directories recursively

Prerequisites

Ensure you have Python installed on your system (Python 3.x recommended).

Installation

Clone this repository or download the script.

Navigate to the project directory:

cd file-integrity-checker

Install required dependencies (if any):

pip install -r requirements.txt  # If additional packages are required in future versions

Usage

Run the script using the command:

python file_integrity_checker.py

Enter the directory you want to monitor.

The tool will check for file changes and report any modifications.

How It Works

On the first run, the script calculates SHA-256 hashes of all files in the given directory and saves them in file_hashes.json.

On subsequent runs, it compares the current hashes with the stored ones to detect changes.

The tool categorizes changes into:

Modified files: Existing files whose content has changed.

New files added: Newly created files.

Deleted files: Files that were removed from the directory.

Example Output

Enter the directory to monitor: /path/to/folder
Modified files:
 - /path/to/folder/file1.txt

New files added:
 - /path/to/folder/newfile.txt

Files deleted:
 - /path/to/folder/oldfile.txt

Notes

Make sure to run the script periodically to check for changes.

Store the file_hashes.json file in a safe place for reliable comparisons.

To reset the stored hashes, simply delete file_hashes.json and rerun the script.
