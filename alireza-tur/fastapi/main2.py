from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import mysql.connector 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
  )
cursor=mydb.cursor()

class Movie(BaseModel):
    name:str
    year:int
    storyline:Optional[str]="nothing"

app = FastAPI()


@app.get("/")
def root():
    return {"message" : "hello"}


@app.get("/all_movies")
def movies():
    sql="SELECT * FROM moive"
    cursor.execute(sql)
    all_movies=cursor.fetchall()
    return all_movies


@app.get("/list_id/{id}")
def list_moive_by_id(id:int):
    sql=f"SELECT * FROM moive WHERE id ={id}"
    cursor.execute(sql)
    movie=cursor.fetchall()
    return movie

@app.get("/list_name/{name}")
def list_moive_by_title(name:str):
    sql="SELECT * FROM moive WHERE name=%s"
    val=(name,)
    cursor.execute(sql,val)
    return cursor.fetchall()[0]


@app.delete("/delete_id/{id}")
def delete_moive_by_id(id:int):
    sql="DELETE FROM moive WHERE id=%s"
    val=(id,)
    cursor.execute(sql,val)
    mydb.commit()
    return {"massege":"ok"}

@app.post("/add")
def add_movie(mov:Movie):
    sql="INSERT INTO moive (name ,year ,storyline) VALUES (%s,%s,%s)"
    val=(mov.name,mov.year,mov.storyline)
    cursor.execute(sql,val)
    mydb.commit()
    return mov


@app.post("/update_id")
def update_movie(id:int,mov:Movie):
    sql="UPDATE moive SET name=%s ,year=%s ,storyline=%s WHERE id=%s"
    val=(mov.name,mov.year,mov.storyline,id)
    cursor.execute(sql,val)
    mydb.commit()
    return {"massege":"ok"}
