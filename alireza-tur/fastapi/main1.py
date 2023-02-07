from fastapi import FastAPI
import mysql.connector 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python"
  )

cursor=mydb.cursor()



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
    all_movies=cursor.fetchall()
    return all_movies

@app.delete("/delete_id/{id}")
def delete_moive_by_id(id:int):
    sql="DELETE FROM moive WHERE id=%s"
    val=(id,)
    cursor.execute(sql,val)
    mydb.commit()
    return {"massege":"ok"}

@app.post("/add")
def add_movie(mov:dict):
    sql="INSERT INTO moive (name ,year ,storyline) VALUES (%s,%s,%s)"
    val=(mov['name'],mov['year'],mov['storyline'])
    cursor.execute(sql,val)
    mydb.commit()
    return mov


@app.post("/update_id")
def update_movie(id:int,mov:dict):
    sql="UPDATE moive SET name=%s ,year=%s ,storyline=%s WHERE id=%s"
    val=(mov['name'],mov['year'],mov['storyline'],id)
    cursor.execute(sql,val)
    mydb.commit()
    return {"massege":"ok"}
