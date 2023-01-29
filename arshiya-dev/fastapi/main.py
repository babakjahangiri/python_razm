from  fastapi import  FastAPI,HTTPException
import mysql.connector
from pydantic import BaseModel
from movie import  Movie

mydb = mysql.connector.connect(host="localhost",user="arshiya",password="arshiya",database="python",port=3306)

mycursor = mydb.cursor()

app = FastAPI()

# movies = [
#           {"title":"","year":0},
#           {"title":"Batman","year":2021},
#           {"title":"joker","year":2022},
#           {"title":"money Hiest","year":2015},
#           {"title":"office","year":2005}]


@app.get("/")
async def root():
    return {"message":"welcome"}

# get all movies
@app.get("/movies")
def get_movies():
    sql = "SELECT * FROM movies"
    mycursor.execute(sql)
    movies = mycursor.fetchall() # function return everything by cursor
    return movies

# get single movie by id
@app.get("/movie/{movie_id}")
def get_movie(movie_id:int):
    sql = "SELECT * FROM movies WHERE id  = %s"
    val = (movie_id,)
    mycursor.execute(sql,val)
    movie = mycursor.fetchall()
    return  movie[0]

@app.get("/movie_by_title/{movie_title}")
def get_movie_by_title(movie_title:str):
    sql = "SELECT * FROM movieS WHERE  title = %s"
    val = (movie_title,)
    mycursor.execute(sql,val)
    movie = mycursor.fetchall()
    if len(movie) == 0:
        raise HTTPException(status_code=500,detail="Movie not found")
    return movie[0]


@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    sql = "DELETE FROM movies WHERE id = %s"
    val = (movie_id,)
    mycursor.execute(sql,val)
    mydb.commit()
    return  {"message":"movie has been deleted successfully"}

# if you want to create or insert new things you have to use post request and post requesat never get parameter like delete
@app.post("/create_movie")
def create_movie(movie:Movie):
    sql = "INSERT INTO movies (title,year,storyline) VALUES (%s,%s,%s)"
    val = (movie.title,movie.year,movie.storyline)
    mycursor.execute(sql,val)
    mydb.commit() # with this function wwe insert data to database
    return movie


#update movie
@app.post("/update_movie")
def update_movie(movie:Movie,move_id):
    sql = "UPDATE movies SET title = %s , year = %s , storyline = %s WHERE  id  = %s"
    val = (movie.title,movie.year,movie.storyline,move_id)
    mycursor.execute(sql,val)
    mydb.commit()
    return movie
    # movie_tobe_updated = movies[movie_id] # get movie to be updated
    # movie_tobe_updated['title'] = movie['title'] # update title
    # movie_tobe_updated['year'] = movie['year'] # update year
    # movies[movie_id] = movie_tobe_updated # has been updated successfully
    # return movie_tobe_updated





