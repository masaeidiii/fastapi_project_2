import sqlite3


query =( """
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT not null,
    country text,
    year INTEGER,
    imdb_rate real,
    image text
)
""")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute(query)
conn.commit()
conn.close()
