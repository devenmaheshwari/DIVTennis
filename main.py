import sqlite3
import pandas as pd
import Tennis
import injuries_to_pd_df
import Weather
import json

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
    Weather JSON
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
    injurydf = injuries_to_pd_df.injury()
    
    #print(injurydf)
    return injurydf

def combine():
    tennis = importTennis()
    injury = importInjury()

    df = pd.concat([tennis, injury], axis=0)

    df['Weather'] = None

    print(df)
    return df


def main():
    df = combine()
    setup()

    conn = sqlite3.connect(DB_FILE)

    test = df[['Date', 'Location']].drop_duplicates()
    test['Weather'] = None

    test = test.head(50)

    testdict = {}

    for index, row in test.iterrows():
        walf = Weather.getWeather(row['Location'], row['Date'])
        test.at[index, 'Weather'] = walf
        testdict[(row['Location'], row['Date'])] = walf


    #print(testdict)

    df['Weather'] = df.apply(lambda row: json.dumps(testdict.get((row['Location'], row['Date']))) if testdict.get((row['Location'], row['Date'])) else None, axis=1)
    #print(df)

    df.to_sql("Data", conn, if_exists='replace', index=False)
    
    conn.commit()
    conn.close()




    # for index, row in df.head(5).iterrows():
    #     #print(index)
    #     #print(row)
    #     #print(row['Location'])
    #     try:
    #         print("Tried")
    #         wata = Weather.getWeather(row['Location'], row['Date'])
    #         print(wata)
    #         df.at[index, 'Weather'] = wata
    #         print
    #     except:
    #         print("Except")
    #         df.at[index, 'Weather'] = {}
    
    # Apply the function directly to each row to populate the 'Weather' column
    # df['Weather'] = df.apply(lambda row: Weather.getWeather(row['Location'], row['Date']), axis=1)
    #print(df)



# This line checks if the script is being run directly
if __name__ == "__main__":
    main()
