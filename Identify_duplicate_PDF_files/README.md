# PDF Duplicate Finder

This script identifies and lists duplicate PDF files within a specified directory, including its subdirectories, by calculating their MD5 hash values.

## Usage

### 1. Clone the repository
Clone this repository to your local machine:
   ```
   git clone https://github.com/Zhuqian-He/Practical-Tools-for-Data-Clean.git
   ```
### 2. Run the script from the command line
Use the following command to run the script from the command line, specifying the directory where you want to check for duplicates:
   ```Bash
   python3 Identify_duplicate_PDF_files_command-line.py "path/to/your/folder"
   ```

### 3. Run the script directly (without command line arguments)
If you prefer to run the script directly without passing arguments via the command line, modify the target_dir variable in the script to point to the folder you want to scan for duplicate PDFs:
   ```python
   target_dir = r".\folder_to_check"
   ```
After modifying the target_dir, run the script using your preferred Python environment or IDE.
Then run the script in your software.

## Requirements
- Python 3.x
- No additional dependencies (uses built-in Python libraries)

## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to your branch (git push origin feature/your-feature).

5. Create a new Pull Request.
