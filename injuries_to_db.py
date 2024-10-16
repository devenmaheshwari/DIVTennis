# ABOUT: file to convert web scraped data into a database file

import sqlite3
from Injury import rows

# convert table to database 

# Injury Date in webpage - Date Column in DB
# Player in Webpage - Player Column in DB
# Injury Description Column in Webage - Tournament Column in DB
# Number 1 - Injury Column in DB

conn = sqlite3.connect("injuries.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS injuries(date TEXT, player TEXT, tournament TEXT, injury INTEGER)''')

for row in rows:
    date_and_player, injury_and_tournament = row.split(" - ", 1) # 1 split only
    
    # split to extract injury and tournament, since type of injury is irrelevant
    injury, tournament = injury_and_tournament.split(" from ", 1)

    # Split the date and player details
    date, player = date_and_player.split(" ", 1)

    player, injury = player.split(") ", 1)
    
    # Insert into database, injury = 1 in all cases 
    cursor.execute('''INSERT INTO injuries(date, player, tournament, injury) VALUES(?, ?, ?, ?)''', (date, player, tournament, 1))
    
conn.commit()
conn.close()