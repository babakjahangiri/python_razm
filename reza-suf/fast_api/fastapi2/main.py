from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/')
async def hello():
    return "hello from Route!"


class TypeBlogs(str, Enum):
    first = 'one'
    second = 'two'
    

@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'], response_description='this is for test')
def get_comment(id:int, comment_id:int, valid:bool=True, username:Optional[str]=None):
    """
    this api for get comment from server
    
    - **id** user id , required
    - **comment_id** comment id, required
    - **valid** optional
    - **username** username, optional
    """
    return {"message": f"blog id {id} comment id {comment_id} {valid=} {username=} "}

@app.get('/blog/all', tags=['blog'], summary='Get all the blogs')
def get_blogs(page:Optional[int]=None, page_size:str=None):
    return {"message": f"{page=} -- {page_size=}"}


@app.get('/blog/type/{type}', tags=['blog'])
def get_type_blog(type:TypeBlogs):
    return {"message":" all blogs!", "type":f"{type}"}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id:int, response:Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Blog {id=} Not Found !"}
    return {"message":f"Blogs! {id}"}
