from  fastapi import  FastAPI
import mysql.connector


mydb = mysql.connector.connect(host="localhost",user="arshiya",password="arshiya",database="python",port=3306)

mycursor = mydb.cursor()

app = FastAPI()

movies = [
          {"title":"","year":0},
          {"title":"Batman","year":2021},
          {"title":"joker","year":2022},
          {"title":"money Hiest","year":2015},
          {"title":"office","year":2005}]


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

# get single movie
@app.get("/movie/{movie_id}")
def get_movie(movie_id:int):
    return  movies[movie_id]


@app.delete("/movie/{movie_id}")
def delete_movie(movie_id:int):
    movies.pop(movie_id)
    return  {"message":"movie has been deleted successfully"}

# if you want to create or insert new things you have to use post request and post requesat never get parameter like delete
@app.post("/create_movie")
def create_movie(movie:dict):
    movies.append(movie)
    return movies[-1]


#update movie
@app.post("/update_movie")
def update_movie(movie_id:int,movie:dict):
    movie_tobe_updated = movies[movie_id] # get movie to be updated
    movie_tobe_updated['title'] = movie['title'] # update title
    movie_tobe_updated['year'] = movie['year'] # update year
    movies[movie_id] = movie_tobe_updated # has been updated successfully
    return movie_tobe_updated





