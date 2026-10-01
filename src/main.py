from fastapi_offline import FastAPIOffline
import sqlite3

app = FastAPIOffline()


# -------------------------------------------------------------
@app.get('/')
def homme():
    return {'welcom':'home'}


@app.get('/allmovies')
def getall_movies():
    all_1 = ('select * from movies')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    movies = cursor.execute(all_1).fetchall()
    
    conn.close()
    return movies

@app.get('/movie/{movies_id}')
def get_movies_id(movies_id:int):
    all_2 = ('select * from movies WHERE id = ?')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    movies = cursor.execute(all_2, (movies_id,)).fetchone()
    
    conn.close()
    return movies

@app.post("/movies")
def create_movies(title : str,
    country : str,
    year : int,
    imdb_rate :float,
    image: str):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO movies (title, country, year, imdb_rate, image) VALUES (?,?,?,?,?)",
        (title,
    country,
    year,
    imdb_rate,
    image))
    
    conn.commit()
    conn.close()
    
    return {
        "message":"monies created"}

@app.delete('/movie/{DELETE_ID}')
def deleted_movies_id(DELETE_ID:int):
    all_2 = ('DELETE from movies WHERE id = ?')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    movies = cursor.execute(all_2, (DELETE_ID,))
    conn.commit()
    conn.close()
    return f'delete shode: {movies}'

@app.put("/update/")
def update_movies(id: int, title : str,
    year : int,
    imdb_rate :float,
    ):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    update = 'UPDATE movies SET title= ? , year= ? , imdb_rate= ? WHERE id = ?'
    
    cursor = conn.cursor()
    
    cursor.execute(
        update,
        (title, year, imdb_rate, id))
    
    conn.commit()
    conn.close()
    
    return {
        "message":"updeted"}