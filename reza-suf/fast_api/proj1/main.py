from fastapi import FastAPI
import mysql.connector
from model import Movie

mydb = mysql.connector.connect(host="localhost", password="", database="fastapi", user="root")
mycursor = mydb.cursor()

app = FastAPI()


# movies = [
#     {'title': 'shutter island', 'year': 2014},
#     {'title': 'Se7en', 'year': 2019},
#     {'title': 'Before','year':2022},
#     {'title': 'sunrise','year':2020},
#     {'title': 'sunset','year':2023},
#     {'title': 'After','year':2021}
# ]


@app.get("/")
async def root():
    return "Home Page"
    

# get movies
@app.get("/movies")
def get_movies():
    sql = "SELECT * FROM movies"
    mycursor.execute(sql)
    movies = mycursor.fetchall()
    return movies

#get movie by id
@app.get("/movies/{movie_id:int}")
def get_movie(movie_id):
    sql = "SELECT * FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)
    movie = mycursor.fetchone()
    # movie = mycursor.fetchall()[0]
    return movie

# delete movies by id
@app.delete('/movies/{movie_id:int}')
def delete_movie(movie_id):
    sql = "DELETE FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message":"movie has been deleted success"}


@app.post("/create_movie")
def create_movie(movie:Movie):
    sql = "INSERT INTO movies (title,year,storyline) VALUES (%s,%s,%s)"
    val = (movie.title, movie.year, movie.storyline)
    mycursor.execute(sql, val)
    mydb.commit()
    return 'Done!'


@app.post("/update_movie")
def update_movie(movie_id:int, movie:Movie):
    sql = "UPDATE movies SET title=%s, year=%s, storyline=%s WHERE id=%s"
    val = (movie.title, movie.year, movie.storyline, movie_id)
    mycursor.execute(sql, val)
    mydb.commit()
    return 'Done!'