from fastapi import APIRouter
from src.models.water_tracker import WaterTracker, CreateWaterTracker
from database.schemas.water_tracker_schema import WaterTrackerSchema
from datetime import date
from typing import List

router = APIRouter()
schema = WaterTrackerSchema()

@router.get("/user/{user_id}/tracker/", response_model=WaterTracker)
async def today_tracker(user_id: str):
    return schema.today_tracker(user_id)

@router.get("/user/{user_id}/tracker/{tracker_date}/", response_model=WaterTracker)
async def get_tracker(user_id: str, tracker_date: date):
    return schema.get_tracker(user_id, tracker_date)

@router.put("/user/{user_id}/tracker/{tracker_date}/", response_model=WaterTracker)
async def tracker_update_consume(user_id: str, tracker_date: date, update: dict):
    return schema.tracker_update_consume(user_id, tracker_date, update)

@router.post("/user/{user_id}/tracker/{tracker_date}/", response_model=WaterTracker)
async def create_specific_tracker(user_id: str, tracker_date: date):
    return schema.create_tracker(user_id, tracker_date)

@router.get("/user/{user_id}/history/", response_model=List[WaterTracker])
async def get_list_trackers(user_id: str):
    return schema.get_trackers(user_id)