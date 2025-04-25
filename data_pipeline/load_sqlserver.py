import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()

# Define SQL Server connection details
server = os.getenv("SQL_SERVER_HOST")
username = os.getenv("SQL_SERVER_USER")
port = os.getenv("SQL_SERVER_PORT", "1433") 
password = os.getenv("SQL_SERVER_PASSWORD") 
driver = "ODBC Driver 17 for SQL Server"

# Load transformed data
df = pd.read_csv("transformed_data.csv")

# Connect to the master DB first
master_url = URL.create(
    "mssql+pyodbc",
    username=username,
    password=password,
    host=server,
    database="master",
    query={"driver": driver}
)
master_engine = create_engine(master_url)

print("Connecting to master DB to check/create warehouse...")

# Create warehouse DB if not exists — with AUTOCOMMIT
with master_engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
    conn.execute(text("""
        IF NOT EXISTS (
            SELECT name FROM sys.databases WHERE name = 'warehouse'
        )
        BEGIN
            CREATE DATABASE warehouse;
        END
    """))
print("Warehouse DB checked/created.")

# Now connect to the warehouse DB
warehouse_url = URL.create(
    "mssql+pyodbc",
    username=username,
    password=password,
    host=server,
    database="warehouse",
    query={"driver": driver}
)
warehouse_engine = create_engine(warehouse_url)

# Upload data to a table
print("Loading data to SQL Server warehouse...")
df.to_sql("user_posts", con=warehouse_engine, if_exists="replace", index=False)
print("Data loaded successfully into 'user_posts' table.")
