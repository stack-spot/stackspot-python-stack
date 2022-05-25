from fastapi import FastAPI, APIRouter
from mangum import Mangum
from src.user import usecase
from src.user.usecase import User

app = FastAPI()
router = APIRouter(tags=["users"], responses={404: {"description": "User not found"}})


@router.post("/user/")
def post_user(user: User):
    return usecase.post_user(user)


@router.delete("/user/{id}")
def delete_user(id):
    return usecase.delete_user(id)


app.include_router(router)
handler = Mangum(app)
