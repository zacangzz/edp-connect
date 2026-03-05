# code for connecting to database using sqlalchemy abstraction

import os
import pyodbc
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

## testing out connecting using SQLAlchemy
def connect_SQLServer():
    load_dotenv()
    driver = "{ODBC Driver 17 for SQL Server}"
    server = os.getenv('SERVER')
    database = os.getenv('DB')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};Authentication=ActiveDirectoryPassword"
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    #print(connection_url)

    try:
        # establishing the connection to the database using engine as an interface
        engine = create_engine(connection_url)
        # wrapping connection using 'with' for compatibility with sqlalchemy 2.x
        with engine.connect() as conn:
            print(f"SQLAlchemy Engine Connected")
    except Exception as e:
        print(f"SQLAlchemy Engine Error.")
        raise
    return engine

# engine_ = connect_SQLServer()
# print(engine_)

if __name__ == "__main__":
    print("This code is not meant to run on it's own")
else:
    print("")