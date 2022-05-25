from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import Optional


class Book(BaseModel):
    id_: int = Field(..., gt=0, title="Id of the book.", description="Must be greater than zero")
    name: str = Field(..., title="The name of the book", max_length=200)
    author: str = Field(..., title="The author's name", max_length=100)
    image_url: Optional[str] = Field(None, title="The author's name", max_length=100)

    class Config:
        schema_extra = {
            "example": {
                "id_": 1,
                "name": "The War of Art",
                "author": "Sun Tzu"
            }
        }


books = [Book(id_=1, name="The War of Art", author="Sun Tzu"),
         Book(id_=2, name="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams")]


def get_book(book_id: int):
    book = next((book for book in books if book.id_ == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


def get_books(book_name):
    result = []
    for book in books:
        if book_name in book.name:
            result.append(book)
    return result
