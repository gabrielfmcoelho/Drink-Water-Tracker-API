from src.models.user import User, CreateUser
from database.database import users_collection
from bson import ObjectId
from fastapi import HTTPException
from typing import List

class UserSchema():
    
    @staticmethod
    def user_serializer(user) -> User:
        user_id = str(user["_id"])
        return User(id=user_id, 
                    name=user["name"], 
                    weight=user["weight"])
    
    def users_serializer(self, users) -> List[User]:
        return [self.user_serializer(user) for user in users]
    
    @staticmethod
    def create_user(user: CreateUser) -> User:
        user_data = {
            "name": user.name,
            "weight": user.weight,
        }
        user_id = users_collection.insert_one(user_data).inserted_id
        user_with_id = user.dict()
        user_with_id["id"] = str(user_id)
        return User(**user_with_id)

    def get_user(self, user_id: str) -> User:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return self.user_serializer(user)