from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    name: str 
    weight: int
    
class User(CreateUser):
    id: Optional[str]
