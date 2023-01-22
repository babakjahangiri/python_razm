from  fastapi import  FastAPI


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
@app.post("/movie")
def create_movie(movie:dict):
    movies.append(movie)
    return movies[-1]



















