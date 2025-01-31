import pandas as pd
import json
import os
import logging
from datetime import datetime
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_cleaning.log'),
        logging.StreamHandler()
    ]
)

class DataCleaner:
    def __init__(self, raw_data_dir='raw_data/archive/archive', db_connection='postgresql://postgres:5492460@localhost:5432/medical_dw'):
        """
        Initialize the DataCleaner with raw data directory and database connection.
        """
        self.raw_data_dir = raw_data_dir
        self.engine = create_engine(db_connection)
        self.processed_files = set()

    def load_raw_data(self):
        """
        Load and merge all JSON files from the raw_data directory.
        """
        all_data = []
        for filename in os.listdir(self.raw_data_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.raw_data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        all_data.extend(data)
                        self.processed_files.add(filename)
                        logging.info(f"Loaded {len(data)} records from {filename}")
                    except json.JSONDecodeError:
                        logging.error(f"Invalid JSON format in {filename}")
                    except Exception as e:
                        logging.error(f"Error loading {filename}: {str(e)}")
        return pd.DataFrame(all_data)

    def clean_data(self, df):
        """
        Perform data cleaning transformations.
        """
        # Remove duplicates
        df = df.drop_duplicates(subset=['message_id', 'channel'], keep='last')
        logging.info(f"Removed duplicates, remaining records: {len(df)}")

        # Handle missing values
        df['text'] = df['text'].fillna('')
        df['media_path'] = df['media_path'].fillna('N/A')
        logging.info("Handled missing values")

        # Standardize formats
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['scrape_timestamp'] = pd.to_datetime(df['scrape_timestamp'])
        logging.info("Standardized date formats")

        # Clean text data
        df['text_clean'] = df['text'].str.strip().str.lower()
        logging.info("Cleaned text data")

        # Data validation
        valid_mask = df['date'].notna() & df['text_clean'].ne('')
        df = df[valid_mask].copy()
        logging.info(f"Applied validation, remaining records: {len(df)}")

        return df

    def save_to_db(self, clean_df):
        """
        Save cleaned data to PostgreSQL database.
        """
        try:
            clean_df.to_sql(
                'raw_medical_data',
                self.engine,
                if_exists='append',
                index=False,
                method='multi'
            )
            logging.info(f"Successfully loaded {len(clean_df)} records to database")
        except Exception as e:
            logging.error(f"Database insertion failed: {str(e)}")

    def archive_raw_files(self):
        """
        Move processed files to archive directory.
        """
        archive_dir = os.path.join(self.raw_data_dir, 'archive')
        os.makedirs(archive_dir, exist_ok=True)
        
        for filename in self.processed_files:
            src = os.path.join(self.raw_data_dir, filename)
            dest = os.path.join(archive_dir, filename)
            os.rename(src, dest)
            logging.info(f"Archived {filename}")

    def run_pipeline(self):
        """
        Execute the full data cleaning pipeline.
        """
        logging.info("Starting data cleaning pipeline")
        
        raw_df = self.load_raw_data()
        logging.info(f"Loaded {len(raw_df)} raw records")
        
        clean_df = self.clean_data(raw_df)
        logging.info(f"Cleaned data contains {len(clean_df)} records")
        
        self.save_to_db(clean_df)
        self.archive_raw_files()
        logging.info("Data cleaning pipeline completed successfully")

if __name__ == '__main__':
    cleaner = DataCleaner()
    cleaner.run_pipeline()