# Ethiopian Medical Businesses Data Pipeline

This project focuses on building a robust data pipeline for Ethiopian medical businesses by scraping data from Telegram channels, cleaning and transforming the data, and storing it in a data warehouse for analysis. The pipeline consists of two main tasks:

1. **Task 1: Data Scraping and Collection Pipeline** - Scrapes data from Telegram channels.
2. **Task 2: Data Cleaning and Transformation** - Cleans and transforms the scraped data using Python and DBT.



## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Task 1: Data Scraping and Collection Pipeline](#task-1-data-scraping-and-collection-pipeline)
4. [Task 2: Data Cleaning and Transformation](#task-2-data-cleaning-and-transformation)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Challenges and Solutions](#challenges-and-solutions)
8. [Next Steps](#next-steps)
9. [Contributing](#contributing)
10. [License](#license)



## **Project Overview**
The goal of this project is to build a data pipeline that:
- Scrapes data from Telegram channels related to Ethiopian medical businesses.
- Cleans and transforms the scraped data.
- Stores the data in a PostgreSQL database for analysis.

The pipeline is designed to be modular, scalable, and easy to maintain.



## **Repository Structure**
```plaintext
project/
├── data_cleaning.py         # Python script for data cleaning
├── telegram_scraper.py      # Python script for Telegram scraping
├── scraping.log            # Logs for the scraping process
├── data_cleaning.log       # Logs for the data cleaning process
├── raw_data/               # Directory for raw scraped data
│   ├── DoctorsET_20231025_143022.json
│   ├── Chemed_20231025_143023.json
│   ├── media/              # Directory for scraped media files
│   │   ├── DoctorsET/
│   │   │   ├── 1.jpg
│   │   │   ├── 2.jpg
│   ├── archive/            # Directory for archived raw files
├── medical_transform/       # DBT project for data transformation
│   ├── models/
│   │   ├── staging/
│   │   │   ├── stg_medical_data.sql
│   │   │   └── schema.yml
│   │   ├── marts/
│   │   │   ├── fact_messages.sql
│   ├── dbt_project.yml      # DBT project configuration
│   ├── profiles.yml         # DBT profiles configuration
```



## **Task 1: Data Scraping and Collection Pipeline**
### **Objective**
Scrape data from Telegram channels, including text and media, and store it in a structured format.

### **Implementation**
- **Tools**: Python (`telethon`, `pandas`, `logging`), Telegram API.
- **Steps**:
  1. Set up Telegram API access using `API_ID` and `API_HASH`.
  2. Scrape data from specified Telegram channels (e.g., DoctorsET, Chemed).
  3. Store raw data in JSON files and media files in a structured directory.
  4. Log all activities for monitoring and debugging.

### **Output**
- Raw data stored in `raw_data/` directory.
- Media files stored in `raw_data/media/`.
- Logs stored in `scraping.log`.



## **Task 2: Data Cleaning and Transformation**
### **Objective**
Clean and transform the scraped data to ensure consistency, remove duplicates, and prepare it for analysis.

### **Implementation**
- **Tools**: Python (`pandas`, `sqlalchemy`), DBT (Data Build Tool).
- **Steps**:
  1. Load raw data from JSON files.
  2. Clean data by removing duplicates, handling missing values, and standardizing formats.
  3. Validate data to ensure quality.
  4. Store cleaned data in a PostgreSQL database.
  5. Use DBT to transform data into analytical models.

### **Output**
- Cleaned data stored in PostgreSQL (`raw_medical_data` table).
- DBT models for staging (`stg_medical_data`) and analytics (`fact_messages`).
- Logs stored in `data_cleaning.log`.



## **Setup and Installation**
### **Clone the Repository**
```bash
git clone https://github.com/Azazh/Medical-Data-Warehouse.git
cd Medical-Data-Warehouse
```

### **Install Python Dependencies**
```bash
pip install -r requirements.txt
```

### **Set Up PostgreSQL Database**
1. Create a database named `medical_dw`.
2. Update the connection string in `data_cleaning.py` and `profiles.yml`.

### **Set Up Telegram API**
1. Obtain `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).
2. Update the credentials in `telegram_scraper.py`.

### **Install DBT**
```bash
pip install dbt-postgres
```



## **Usage**
### **Run the Scraping Script**
```bash
python telegram_scraper.py
```

### **Run the Data Cleaning Script**
```bash
python data_cleaning.py
```

### **Run DBT Transformations**
```bash
cd medical_transform
dbt run --models marts
dbt test
dbt docs generate
dbt docs serve
```



## **Challenges and Solutions**
| Challenge | Solution |
|--|-|
| Rate limits on Telegram API | Implemented rate limiting and retries in the scraping script. |
| Inconsistent data formats in Telegram messages | Standardized text and date formats during cleaning. |
| Duplicate messages in scraped data | Removed duplicates based on `message_id` and channel. |



## **Next Steps**
- **Task 3**: Implement object detection using YOLO for media files.
- **Task 4**: Design and implement the data warehouse schema.
- **Task 5**: Integrate data enrichment and advanced analytics.



## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.



## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## **Contact**
For questions or feedback, please contact:
- **azazh w**  
- **azazhwuletaw@gmail.com**  
- **https://github.com/azazh**
