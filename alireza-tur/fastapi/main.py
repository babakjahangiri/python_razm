from fastapi import FastAPI

app = FastAPI()

all_movies=[
    {"name":"batman","year":2021,"time":120},
    {"name":"adams","year":2011,"time":100},
    {"name":"joker","year":2020,"time":1020},
    {"name":"ice age","year":2000,"time":150}
    ]

@app.get("/")
def root():
    return {"message" : "hello"}


@app.get("/blogs")
def blogs():
    return {"massage":"blogs"}

@app.get("/all_movies")
def movies():
    return all_movies


@app.get("/list_id/{id}")
def list_moive_by_id(id:int):
    return all_movies[id]

@app.delete("/delete_id/{id}")
def delete_moive_by_id(id:int):
    all_movies.pop(id)
    return {"massege":"ok"}

@app.post("/add")
def add_movie(mov:dict):
    all_movies.append(mov)
    return all_movies


@app.post("/update_id")
def update_movie(id:int,mov:dict):
    all_movies[id]=mov
    return {"massege":"ok"}
