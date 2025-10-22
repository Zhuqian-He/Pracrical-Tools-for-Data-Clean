import os
import argparse
import logging

def create_year_folders(base_path, start_year, end_year):
    """Create empty folders named by year in the specified directory"""
    # Validate year range
    if start_year > end_year:
        logging.error(f"Invalid year range: Start year ({start_year}) is greater than end year ({end_year})")
        return

    # Create base directory if it doesn't exist
    try:
        os.makedirs(base_path, exist_ok=True)
        logging.info(f"Ensured base directory exists: {base_path}")
    except Exception as e:
        logging.error(f"Failed to create base directory {base_path}: {str(e)}")
        return

    # Create folder for each year in range
    for year in range(start_year, end_year + 1):
        folder_path = os.path.join(base_path, str(year))
        try:
            os.makedirs(folder_path, exist_ok=True)
            logging.info(f"Created/Verified folder: {folder_path}")
        except Exception as e:
            logging.error(f"Failed to process folder {folder_path}: {str(e)}")

def main():
    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Create empty year-named folders in a specified path')
    parser.add_argument('target_path', help='Target directory path to create year folders')
    parser.add_argument('start_year', type=int, help='Start year (e.g., 1969)')
    parser.add_argument('end_year', type=int, help='End year (e.g., 2018)')
    
    args = parser.parse_args()

    # Log start information
    logging.info("Starting year folder creation process...")
    logging.info(f"Target directory: {os.path.abspath(args.target_path)}")
    logging.info(f"Year range: {args.start_year} - {args.end_year}")

    # Create folders
    create_year_folders(args.target_path, args.start_year, args.end_year)

    logging.info("Folder creation process completed")

if __name__ == "__main__":
    main()