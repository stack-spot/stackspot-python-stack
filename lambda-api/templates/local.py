from uvicorn import run
from fastapi import FastAPI
from src.user.controller import router as user_router

app = FastAPI()
app.include_router(user_router)

if __name__ == "__main__":
    run("local:app", host='127.0.0.1', port=8080, reload=True)
