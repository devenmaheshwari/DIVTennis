"""
Program to take in the atp_tennis.csv data and convert it into a db file
"""

import pandas as pd
import sqlite3

def csv_to_sql(csv_file, db_name, table_name):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Connect to the SQLite database (it will be created if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Write the DataFrame to a SQL table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Commit and close the connection
    conn.commit()
    conn.close()

    print(f"CSV data has been successfully inserted into the {table_name} table in {db_name} database.")

# Example usage
csv_file = 'atp_tennis.csv'      # Path to your CSV file
db_name = 'tennis.db'    # Name of your SQLite database file
table_name = 'entries'       # Desired table name in the database

csv_to_sql(csv_file, db_name, table_name)
