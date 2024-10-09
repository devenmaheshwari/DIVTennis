import sqlite3

DB_FILE = "Submission.db"

def setup():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("DROP TABLE IF EXISTS data")
    command = "CREATE TABLE data (count PRIMARY KEY AUTOINCREMENT, date DATE, player VARCHAR(50), tournament VARCHAR(50)), surface VARCHAR(50), weather JSON, injured INT"
    c.execute(command)

    db.commit()
    db.close()

# gets all entries of specific player
def get_playre(player):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    username = None
    c.execute("SELECT player FROM users WHERE username=?", [player])
    row = c.fetchone()
    if row is not None:
        username = row[0]

    return username