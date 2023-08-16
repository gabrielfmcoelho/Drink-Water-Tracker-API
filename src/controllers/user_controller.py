from fastapi import APIRouter
from src.models.user import User, CreateUser
from database.schemas.user_schema import UserSchema
from database.database import users_collection

router = APIRouter()
schema = UserSchema()

@router.post("/user/", response_model=User)
async def create_user(user: CreateUser):
    return schema.create_user(user)

@router.get("/user/{user_id}/", response_model=User)
async def get_user(user_id: str):
    return schema.get_user(user_id)

@router.get("/users/", response_model=list[User])
async def get_users():
    users = users_collection.find()
    return schema.users_serializer(users)