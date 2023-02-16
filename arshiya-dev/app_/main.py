import uvicorn
from fastapi import FastAPI , Body,Depends
from model import PostSchema
from model import PostSchema , UserSchema,UserLoginShema
from auth.jwt_handler import sign_jwt
from auth.jwt_bearer import jwt_auth


posts = [
    {
        "id":1,
        "title":"lions",
        "content": "lions are brave",
    },
    {
        "id":2,
        "title":"Tigers",
        "content": "Tigers are orange and beautiful"
    }
]


users = []


app = FastAPI()


#1-> Test
@app.get("/",tags=['test'])
def root():
    return {"hello":"wlecome to this page"}

#2-> Get posts
@app.get("/posts",tags=["posts"])
def  get_posts():
    return {'date':posts}



#3-> Get single Post{id}
@app.get("/posts/{id}",tags=["posts"])
def get_post_by_id(id:int):
    if id > len(posts):
        return {
            "error":"post with this id does not exist"
        }
    for post in posts:
        if post["id"] == id:
            return {
                "data":post
            }
    
# 4 Post a BLOG POST {HANDLER FOR CREATEING POST}
@app.post("/posts",dependencies=[Depends(jwt_auth)],tags=["posts"])
def create_post(post:PostSchema):
    post.id - len(posts) + 1
    posts.append(post.dict())
    return {
        "info":"post created successfully",
    }


# 5 users sign up [create a user]
@app.post("users/signup",tags=["users"])
def user_sign_up(user:UserSchema = Body(default=None)):
    users.append(user)
    return sign_jwt(user.email)

def check_user(data:UserLoginShema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        else:
            return False

@app.post("users/login",tags=["users"])
def user_login(user:UserLoginShema = Body(default=None)):
    if check_user(user):
        return sign_jwt(user.email)
    else:
        return {
            "error":"invalid email or password"
        }
    