from typing import List
from fastapi import FastAPI, APIRouter
from src.book.usecase import Book
from mangum import Mangum
from src.book import usecase

app = FastAPI()
router = APIRouter(tags=["books"])


@router.get("/books/{id}", response_model=Book, responses={404: {"description": "Book not found"}})
def get_book(id: int):
    return usecase.get_book(id)


app.include_router(router)
handler = Mangum(app)
