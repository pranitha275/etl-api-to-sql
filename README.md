ETL API to SQL - Project Documentation
This project demonstrates a complete ETL (Extract, Transform, Load) pipeline that:
•	- Extracts data from a public API
•	- Transforms the data using Python and Pandas
•	- Loads it into both PostgreSQL and SQL Server databases using SQLAlchemy


Project Structure
etl-api-to-sql/
│
├── data_pipeline/
│   ├── extract.py            # Extracts data from public APIs
│   ├── transform.py          # Transforms and merges the extracted data
│   ├── load_postgres.py      # Loads transformed data into PostgreSQL
│   ├── load_sqlserver.py     # Loads transformed data into SQL Server
│   ├── posts.json            # Raw posts data
│   ├── users.json            # Raw users data
│   ├── transformed_data.csv  # Transformed output saved to CSV
│   ├── requirements.txt      # Python dependencies
│   ├── Dockerfile            # Docker image setup
│   ├── docker-compose.yml    # Compose services (DB, app)
│   └── .env                  # DO NOT COMMIT THIS - Holds environment variables
│
└── .gitignore                # Git ignore rules

 
 How It Works
-Extract: Fetches posts and users data from JSONPlaceholder.
-Transform: Joins user info with posts, cleans fields, saves to CSV.
-Load: Uploads CSV data to PostgreSQL and SQL Server tables.
 
 
Getting Started
1. Clone the repo:
git clone https://github.com/pranitha275/etl-api-to-sql.git
cd etl-api-to-sql/data_pipeline

3. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate

4. Install dependencies:
pip install -r requirements.txt

5. Create a .env file:
# SQL Server
SQL_SERVER_HOST=localhost
SQL_SERVER_PORT=1433
SQL_SERVER_USER=YOUR USERNAME
SQL_SERVER_PASSWORD=Your PASSWORD
SQL_SERVER_DB=DB NAME

# PostgreSQL
PG_USER=USERNAME
PG_PASSWORD=your_pg_password
PG_HOST=localhost
PG_PORT=5432
PG_DB= DB NAME

5. Run the pipeline:
python extract.py
python transform.py
python load_postgres.py
python load_sqlserver.py

