from fastapi import APIRouter
from repository import BookRepo
from model import Book,Response

router = APIRouter()


@router.get("/book/")
async def get_all_book():
    _booklist = await BookRepo.retrieve()
    return Response(code=200,status="ok",message="Success retrieve all data",result=_booklist).dict(exclude_none=True)

@router.post("/book/create")
async def create(book:Book):
    await BookRepo.insert(book)
    return Response(code=200,status="ok",message="Success save all data").dict(exclude_none=True)


@router.get("/book/{id}")
async def get_id(id:str):
    _book =  await BookRepo.retrieve_id(id)
    return Response(code=200,status="ok",message="Success retrieve data",result=_book).dict(exclude_none=True)


@router.post("/book/update")
async def update(book:Book):
    await BookRepo.update(book.id)
    return Response(code=200,status="ok",message="Success update data").dict(exclude_none=True)

@router.delete("/book/{id}")
async def delete(id:str):
    await BookRepo.delete(id)
    return Response(code=200,status="ok",message="Success delete data").dict(exclude_none=True)
