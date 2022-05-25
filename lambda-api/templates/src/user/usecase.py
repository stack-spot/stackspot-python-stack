from fastapi import HTTPException
from pydantic import BaseModel, Field


class User(BaseModel):
    id_: int = Field(..., gt=0, title="Id of the user.", description="Must be greater than zero")
    name: str = Field(..., title="The name of the user", max_length=200)
    age: int = Field(..., gt=0, lt=130, title="The user's age",
                     description="Must be greater than zero and less then 130")

    class Config:
        schema_extra = {
            "example": {
                "id_": 1,
                "name": "John Doe",
                "age": 33
            }
        }


users = [User(id_=1, name="John Doe", age=33),
         User(id_=2, name="Jane Smith", age=26)]


def post_user(user: User):
    return user


def delete_user(user_id: int):
    for user in users:
        if user.id_ == int(user_id):
            return f"User {user_id} deleted!"
    raise HTTPException(status_code=404, detail="User not found")
