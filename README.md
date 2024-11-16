# File Verification Tool

## Overview
The File Verification Tool is a simple graphical user interface (GUI) application designed to help you verify the integrity of files by comparing their computed checksum (MD5 or SHA-256) with a known checksum. It also allows you to calculate the checksum of any file.

## Features
- **Browse Files**: Select files from your system using the file browser.
- **Checksum Algorithms**: Supports MD5 and SHA-256 checksum algorithms.
- **Compute Checksum**: Calculate the checksum of any file.
- **Verify File**: Compare the computed checksum with a provided checksum to check for file integrity.

## Requirements
- Python 3.x
- Required libraries:
  - `tkinter` (standard library, included with Python)
  - `hashlib` (standard library, included with Python)

## How to Use
1. **Launch the Tool**:
   - Run the tool by executing the Python script.
2. **Select a File**:
   - Use the "Browse" button to select the file you want to verify or calculate the checksum for.
3. **Choose an Algorithm**:
   - Select either MD5 or SHA-256 from the dropdown menu.
4. **Compute Checksum**:
   - Click the "Compute Checksum" button to calculate and display the checksum for the selected file.
5. **Verify File**:
   - Enter a known checksum value in the provided field.
   - Click the "Verify File" button to compare the entered checksum with the computed checksum.
   - The tool will notify you if the checksum matches or not.

## Supported Platforms
- Windows (Primary)
- Compatible with other operating systems that support Python and Tkinter.

## Notes
- Ensure the checksum you are verifying against is accurate and from a trusted source.
- Use MD5 for basic checksum validation, but SHA-256 is recommended for higher security and integrity verification.

## License
This tool is released under the MIT License. Feel free to use, modify, and distribute the tool as per the terms of the license.


