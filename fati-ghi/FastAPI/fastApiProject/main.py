from fastapi import FastAPI, HTTPException
import mysql.connector
from fastapi.openapi.models import Response
from pydantic import BaseModel
from models import Movie

mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="python")
mycursor = mydb.cursor()

app = FastAPI()

# movies = [{"title":"", "year":0},
#           {"title":"batman", "year":2021},
#           {"title":"sandman", "year":1999},
#           {"title":"sopranos", "year":2000},
#           {"title":"cindrella", "year":2020},
#           {"title":"joker", "year":2022}]




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/movies")
def get_movies():
    sql = "SELECT * FROM movies"
    mycursor.execute(sql)
    movies = mycursor.fetchall()
    return movies

@app.get("/movie/{movie_id}")
def get_movie(movie_id:int):
    sql = "SELECT * FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql,val)
    movie = mycursor.fetchall() #[[]]
    return movie[0]

@app.get("/movie_by_title/{movie_title}")
def get_movie_by_title(movie_title:str):
    sql = "SELECT * FROM movies WHERE title = %s"
    val = (movie_title,)
    mycursor.execute(sql,val)
    movie = mycursor.fetchall()
    if len(movie) == 0:
        raise HTTPException(status_code=500, detail="movie not found")
    return movie[0]

@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    sql = "DELETE * FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return {"message": "movie has been deleted"}

@app.post("/create_movie")
def create_movie(movie:Movie):
    sql = "INSERT INTO movies (title,year,storyline) VALUES (%s,%s,%s)"
    val = (movie.title, movie.year, movie.storyline)
    mycursor.execute(sql, val)
    mydb.commit()
    return movie

@app.post("/update_movie")
def update_movie(movie:Movie, movie_id:int):
    sql = "UPDATE movies SET title = %s , year = %s , storyline = %s WHERE id = %s"
    val = (movie.title, movie.year, movie.storyline, movie_id)
    mycursor.execute(sql, val)
    mydb.commit()
    return movie
    # movie_to_be_updated = movies[movie_id]
    # movie_to_be_updated['title'] = movie['title']
    # movie_to_be_updated['year'] = movie['year']
    # movies[movie_id] = movie_to_be_updated
    # return movie_to_be_updated
