import os
import argparse

def create_files_in_subdirs(root_dir, filename):
    # Check if root directory exists
    if not os.path.isdir(root_dir):
        print(f"Error: Directory not found - {root_dir}")
        return

    # Iterate through items in root directory
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        # Process only subdirectories
        if os.path.isdir(item_path):
            target_path = os.path.join(item_path, filename)
            # Create file if it doesn't exist
            if not os.path.exists(target_path):
                with open(target_path, 'w', encoding='utf-8') as f:
                    pass  # Empty file
                print(f"Created: {target_path}")
            else:
                print(f"Exists, skipped: {target_path}")

    print("Operation completed")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Create specified file in all subdirectories')
    parser.add_argument('root_dir', help='Root directory path')
    parser.add_argument('filename', help='Name of file to create (e.g., Summary.txt)')
    args = parser.parse_args()

    # Execute file creation
    create_files_in_subdirs(args.root_dir, args.filename)

if __name__ == "__main__":
    main()