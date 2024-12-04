# view submission.db

import sqlite3
import pandas as pd

# connect to database

conn = sqlite3.connect("Submission.db")

query = "SELECT Surface, Injury FROM Data"

df = pd.read_sql_query(query, conn)

# counting injuries per surface type
grouped_data = df.groupby(['Surface', 'Injury']).size().reset_index(name='Count')

# extract all the counts for the chart
count_injured_hard = grouped_data[(grouped_data['Surface'] == 'Hard') & (grouped_data['Injury'] == 1)]['Count'].values[0] 
count_non_injured_hard = grouped_data[(grouped_data['Surface'] == 'Hard') & (grouped_data['Injury'] == 0)]['Count'].values[0]

count_injured_clay = grouped_data[(grouped_data['Surface'] == 'Clay') & (grouped_data['Injury'] == 1)]['Count'].values[0]
count_non_injured_clay = grouped_data[(grouped_data['Surface'] == 'Clay') & (grouped_data['Injury'] == 0)]['Count'].values[0]

count_injured_grass = grouped_data[(grouped_data['Surface'] == 'Grass') & (grouped_data['Injury'] == 1)]['Count'].values[0]
count_non_injured_grass = grouped_data[(grouped_data['Surface'] == 'Grass') & (grouped_data['Injury'] == 0)]['Count'].values[0]

# Check by printing all counts
print(f"Count of injured players on Hard surface: {count_injured_hard}")
print(f"Count of non-injured players on Hard surface: {count_non_injured_hard}")
print(f"Count of injured players on Clay surface: {count_injured_clay}")
print(f"Count of non-injured players on Clay surface: {count_non_injured_clay}")
print(f"Count of injured players on Grass surface: {count_injured_grass}")
print(f"Count of non-injured players on Grass surface: {count_non_injured_grass}")

