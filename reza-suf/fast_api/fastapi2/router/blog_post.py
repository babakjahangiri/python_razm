from fastapi import APIRouter, status, Response, Query, Body, Path
from typing import Optional, List
from pydantic import BaseModel


router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    id : int
    published: Optional[bool]


@router.post('/new/{id}')
def create_blog(blog:BlogModel, id:int, version:int=1):
    return {"message": "Ok", "blog":blog}


@router.post('/new/{id}/comment')
def create_comment(id: int, blog: BlogModel, 
                   comment_title: str = Query(None,
                                              description='Description Text!',
                                              alias='CommentTitle',
                                              deprecated=True),
                   content: str = Body('this is dafault and convet the arg to optional',
                                       min_length=5,
                                       regex=None),
                   comment_id: int = Path(None,
                                          gt=12),
                   myitems: Optional[List[str]] = Query(None)
                   ):
    return {
        "blog": blog,
        "id":id,
        "comment_title":comment_title,
        "content":content,
        "comment_id": comment_id 
    }