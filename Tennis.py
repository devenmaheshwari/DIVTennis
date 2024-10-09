"""
Program to take in the atp_tennis.csv data and convert it into a db file
"""

import pandas as pd
import sqlite3

def csv_to_sql(csv_file, db_name, table_name):
    # Load the CSV file into a DataFrame
    df1 = pd.read_csv(csv_file)
    df1.drop(columns=["Player_2", "Court", "Round", "Series", "Rank_1", "Rank_2", "Pts_1", "Pts_2", "Odd_1", "Odd_2", "Score", "Winner", "Best of"], inplace=True)
    df1.rename(columns={"Player_1": "Player"}, inplace=True)

    df2 = pd.read_csv(csv_file)
    df2.drop(columns=["Player_1", "Court", "Round", "Series", "Rank_1", "Rank_2", "Pts_1", "Pts_2", "Odd_1", "Odd_2", "Score", "Winner", "Best of"], inplace=True)
    df2.rename(columns={"Player_2": "Player"}, inplace=True)

    frames = [df1, df2]

    df = pd.concat(frames)
    print(df)
    df = df.iloc[:,[1, 0, 3, 2]]
    df = df.iloc[:,[0, 2, 1, 3]]
    df.insert(4, "Injury", 1, True)

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
