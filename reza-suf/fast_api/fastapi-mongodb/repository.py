from model import Book
from config import database
from uuid import uuid4


class BookRepo:

    @staticmethod
    async def retrieve():
        _book = []
        collection = database.get_collection('book').find()
        async for book in collection:
            _book.append(book)
        return _book

    @staticmethod
    async def insert(book: Book):
        id = str(uuid4())
        _book = {
            "_id": id,
            "title": book.title,
            "description": book.description
        }
        await database.get_collection('book').insert_one(_book)

    @staticmethod
    async def update(id: str, book: Book):
        _book = await database.get_collection('book').find_one({"_id": id})
        _book["title"] = book.title
        _book["description"] = book.description
        await database.get_collection('book').update({"_id": id}, {"$set": _book})

    @staticmethod
    async def delete(id: str):
        await database.delete_collection('book').delete_one({"_id": id})
