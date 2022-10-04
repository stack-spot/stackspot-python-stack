from uvicorn import run
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    run("local:app", host='127.0.0.1', port=8080, reload=True)
