# ABOUT: converting web scraped data to a Pandas dataframe

import pandas as pd
from Injury import rows # list of strings containing scraped data

# create a dictionary to store the relevant data
data = {"date": [], "player": [], "tournament": [], "injury": []}

for row in rows:
    date_and_player, injury_and_tournament = row.split(" - ", 1) # 1 split only
    
    # split to extract injury and tournament, since type of injury is irrelevant
    injury, tournament = injury_and_tournament.split(" from ", 1)

    # Split the date and player details
    date, player = date_and_player.split(" ", 1)

    player, injury = player.split(") ", 1)
    
    # Insert into database, injury = 1 in all cases 
    data["date"].append(date)
    data["player"].append(player)
    data["tournament"].append(tournament)
    data["injury"].append(1)
    
df = pd.DataFrame(data)

print(df.head())