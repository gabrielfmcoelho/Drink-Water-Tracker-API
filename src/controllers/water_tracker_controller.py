from fastapi import APIRouter
from src.models.water_tracker import WaterTracker, CreateWaterTracker
from database.schemas.water_tracker_schema import WaterTrackerSchema
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from typing import List

router = APIRouter()
schema = WaterTrackerSchema()

@router.get("/user/{user_id}/tracker/", response_model=WaterTracker, tags=["tracker"])
async def today_tracker(user_id: str):
    return schema.today_tracker(user_id)

@router.get("/user/{user_id}/tracker/{tracker_date}/", response_model=WaterTracker, tags=["tracker"])
async def get_tracker(user_id: str, tracker_date: date):
    """_summary_

    Args:
        user_id (str): _descrpiption_
        tracker_date (date): _description_

    Returns:
        _type_: _description_
    """
    return schema.get_tracker(user_id, tracker_date)

@router.put("/user/{user_id}/tracker/{tracker_date}/", response_model=WaterTracker, tags=["tracker"])
async def update_tracker_consume(user_id: str, tracker_date: date, update: dict):
    """_summary_

    Args:
        user_id (str): _description_
        tracker_date (date): _description_
        update (dict): _description_

    Returns:
        _type_: _description_
    """
    return schema.tracker_update_consume(user_id, tracker_date, update)

@router.post("/user/{user_id}/tracker/{tracker_date}/", response_model=WaterTracker, tags=["tracker"])
async def create_specific_tracker(user_id: str, tracker_date: date):
    """_summary_

    Args:
        user_id (str): _description_
        tracker_date (date): _description_

    Returns:
        _type_: _description_
    """
    return schema.create_tracker(user_id, tracker_date)

@router.get("/user/{user_id}/history/", response_model=List[WaterTracker], tags=["tracker"])
async def list_trackers(user_id: str):
    """_summary_

    Args:
        user_id (str): _description_

    Returns:
        _type_: _description_
    """
    return schema.get_trackers(user_id)