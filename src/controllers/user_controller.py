from fastapi import APIRouter
from src.models.user import User, CreateUser
from database.schemas.user_schema import UserSchema
from fastapi.middleware.cors import CORSMiddleware
from database.database import users_collection
from typing import List

router = APIRouter()
schema = UserSchema()


@router.post("/user/", response_model=User, tags=["user"])
async def create_user(user: CreateUser):
    """
    Summary: Create a new user in database

    Args:
        user (CreateUser): User data {name: str, weight: int}

    Returns:
        User: User data with id
    """
    return schema.create_user(user)

@router.get("/user/{user_id}/", response_model=User, tags=["user"])
async def get_user(user_id: str):
    """
    Summary: Get user data by id in database and return user data

    Args:
        user_id (str): User id

    Returns:
        User: User data with id
    """
    return schema.get_user(user_id)

@router.get("/users/", response_model=List[User], tags=["user"])
async def list_users():
    """
    Summary: Get all users data in database and return users data

    Returns:
        List[User]: List of users data with id
    """
    users = users_collection.find()
    return schema.users_serializer(users)