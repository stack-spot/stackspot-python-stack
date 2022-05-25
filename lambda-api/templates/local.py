import uvicorn
from fastapi import FastAPI
from src.user.controller import router as user_router
from src.book.controller import router as book_router

app = FastAPI()
app.include_router(user_router)
app.include_router(book_router)

if __name__ == "__main__":
    uvicorn.run("local:app", host='127.0.0.1', port=8080, reload=True)
