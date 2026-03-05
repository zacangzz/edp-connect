# edp-connect
this is a simple code base to modularise connecting to a database

# Installation Guide

## How to Install
1. In Command Prompt, navigate to the package folder where this README file is residing
    ```bash
    edp_connect/
    │── edp_connect/
    │   ├── __init__.py
    │   ├── connect.py
    │── .env
    │── README.md
    │── pyproject.toml   
    │── setup.py         
    │── requirements.txt
    │── # this is where you navigate to on 

2. Run the following command:
    ```sh
    pip install -e .

## How to Use
1. Copy .env file to your project folder
    ```bash
    edp_connect/
    │── edp_connect/
    │   ├── __init__.py
    │   ├── connect.py
    │── .env                # copy this to your project
    │── README.md
    │── pyproject.toml   
    │── setup.py         
    │── requirements.txt
    ```

    ###Here's whats in your .env file:
    ```ini
    ### .env file for environment variables:
    DRIVER='{ODBC Driver 17 for SQL Server}'
    SERVER='-'
    DB='-'
    DB_USER='-' 
    DB_PASSWORD='-'
    ```

2. Import the package:
    ```python
    from edp_connect import connect as c
3. Connect to SQL Server:
    ```python
    edp_connection = c.connect_SQLServer()
4. Use established connection to pass SQL queries for data extraction: sample code
    ```python
    df = pd.read_sql("SELECT * FROM <schema>.<tablename>",edp_connection)