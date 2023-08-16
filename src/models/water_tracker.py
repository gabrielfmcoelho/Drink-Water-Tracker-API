from pydantic import BaseModel
from datetime import date
from typing import Optional
from bson import ObjectId

class CreateWaterTracker(BaseModel):
    id_owner: str
    weight_at_time: int
    date: date
    goal: int
    missing: int
    consumed: int
    goal_percent: float
    goal_reached: bool

class WaterTracker(CreateWaterTracker):
    id: Optional[str]