# Objective: Identify and list duplicate PDF files within a specified directory, including its subdirectories.

import os
import hashlib
import argparse

def get_file_hash(file_path, block_size=65536):
    """Calculate the MD5 hash of a file (used to check if the content is identical)"""
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            # Read the large file in chunks to avoid high memory usage
            block = f.read(block_size)
            while block:
                hasher.update(block)
                block = f.read(block_size)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Unable to read file {file_path}, error: {e}")
        return None

def find_duplicate_pdfs(directory):
    """Find duplicate PDF files in the directory (including subfolders)"""
    # Dictionary to store the hash values and corresponding file paths: {hash_value: [file_path1, file_path2, ...]}
    hash_map = {}
    
    # Recursively walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Process only PDF files (case-insensitive)
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                # Calculate the file hash
                file_hash = get_file_hash(file_path)
                if file_hash:
                    # Add the file path to the list corresponding to the hash value
                    if file_hash in hash_map:
                        hash_map[file_hash].append(file_path)
                    else:
                        hash_map[file_hash] = [file_path]
    
    # Filter out the duplicate file groups (hash value corresponding to multiple file paths)
    duplicates = {hash_val: paths for hash_val, paths in hash_map.items() if len(paths) > 1}
    return duplicates

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Find duplicate PDF files in a specified directory.")
    parser.add_argument('directory', metavar='directory', type=str, 
                        help="Directory to check for duplicate PDF files")
    args = parser.parse_args()

    target_dir = args.directory

    # Check if the directory exists
    if not os.path.exists(target_dir):
        print(f"Error: Folder does not exist - {target_dir}")
    else:
        print(f"Checking for duplicate PDF files in {target_dir}...\n")
        duplicate_groups = find_duplicate_pdfs(target_dir)
        
        if duplicate_groups:
            print(f"Found {len(duplicate_groups)} group(s) of duplicate PDF files:\n")
            for i, (hash_val, paths) in enumerate(duplicate_groups.items(), 1):
                print(f"Group {i} (exactly identical content):")
                for path in paths:
                    print(f"  - {path}")
                print()  # Empty line to separate different groups
        else:
            print("No duplicate PDF files found.")
