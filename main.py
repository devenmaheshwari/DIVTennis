import sqlite3
import pandas as pd
import Tennis

DB_FILE = "Submission.db"

# Queries
drop_table_query = '''
DROP TABLE IF EXISTS Data;
'''

create_table_query = '''
CREATE TABLE IF NOT EXISTS Data (
    Date DATE NOT NULL,
    Player VARCHAR(50) NOT NULL,
    Tournament VARCHAR(200) NOT NULL,
    Location VARCHAR(100),
    Surface VARCHAR(50),
    Injury INTEGER
);
'''

def setup():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute(drop_table_query)
    c.execute(create_table_query)

    db.commit()
    db.close()

    print("Table dropped and created successfully.")

# gets all entries of specific player
def get_players(player):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    username = None
    c.execute("SELECT player FROM users WHERE username=?", [player])
    row = c.fetchone()
    if row is not None:
        username = row[0]

    return username

def importTennis():
    tennisdf = Tennis.tennis()
    
    #sample_weather = ["weather_code", "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "daylight_duration", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant"]
    #tennisdf.insert(5, "WEATHER", sample_weather, True)
    #print(tennisdf)
    return tennisdf

def importInjury():
    return 1

def getWeather():
    return 1

importTennis()