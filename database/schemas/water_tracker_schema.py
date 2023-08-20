from src.models.water_tracker import WaterTracker
from database.database import trackers_collection, users_collection
from bson import ObjectId
from fastapi import HTTPException
from datetime import datetime, date
from typing import List

class WaterTrackerSchema():
    
    def verify_last_tracker(self, user_id: str):
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        last_tracker = trackers_collection.find_one({"id_owner": user_id}, sort=[("date", -1)])
        if last_tracker is not None:
            last_tracker["id"] = str(last_tracker["_id"])
            return self.tracker_serializer(last_tracker)
        return None
    
    def create_tracker(self, user_id: str, tracker_date: date) -> WaterTracker:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        tracker_on_date = self.get_tracker(user_id, tracker_date, skip_404=True)
        if tracker_on_date is not None:
            raise HTTPException(status_code=409, detail="Tracker already exists")
        if tracker_date > datetime.now().date():
            raise HTTPException(status_code=409, detail="Invalid date")
        to_drink = user["weight"] * 35
        tracker = {
            "id_owner": user_id,
            "weight_at_time": user["weight"],
            "date": tracker_date.strftime("%Y-%m-%d"),
            "goal": to_drink,
            "missing": to_drink,
            "consumed": 0,
            "goal_percent": 0,
            "goal_reached": False,
        }
        tracker_id = trackers_collection.insert_one(tracker).inserted_id
        tracker_with_id = tracker.copy()
        tracker_with_id["id"] = str(tracker_id)
        return self.tracker_serializer(tracker_with_id)
    
    def today_tracker(self, user_id: str) -> WaterTracker:
        last_tracker = self.verify_last_tracker(user_id)
        today = datetime.now().date()
        if (last_tracker is None) or (last_tracker.date < today):
            return self.create_tracker(user_id, today)
        return last_tracker
    
    def get_tracker(self, user_id: str, tracker_date: date, skip_404: bool = False) -> WaterTracker:
        tracker = trackers_collection.find_one({"id_owner": user_id, "date": tracker_date.strftime("%Y-%m-%d")})
        if tracker is None:
            if skip_404:
                return None
            raise HTTPException(status_code=404, detail="Tracker not found")
        return self.tracker_serializer(tracker)

    @staticmethod
    def tracker_serializer(tracker) -> WaterTracker:
        tracker_id = tracker["_id"]
        return WaterTracker(
            id=str(tracker_id),
            id_owner=str(tracker["id_owner"]),
            weight_at_time=tracker["weight_at_time"],
            date=tracker["date"],
            goal=tracker["goal"],
            missing=tracker["missing"],
            consumed=tracker["consumed"],
            goal_percent=tracker["goal_percent"],
            goal_reached=tracker["goal_reached"],
        )
        
    def trackers_serializer(self, trackers) -> List[WaterTracker]:
        return [self.tracker_serializer(tracker) for tracker in trackers]
    
    def tracker_update_consume(self, user_id: str, tracker_date: date, update: dict) -> WaterTracker:
        #tracker_date = datetime.strptime(tracker_date, "%Y-%m-%d").date()
        tracker = self.get_tracker(user_id, tracker_date)
        quantity = update["cupsize"]
        consumed = tracker.consumed + quantity
        missing = tracker.missing - quantity
        if missing <= 0:
            missing = 0
            goal_reached = True
        else:
            goal_reached = False
        goal_percent = round((consumed / tracker.goal) * 100, 2)     
        tracker_data = {
            "id_owner": tracker.id_owner,
            "weight_at_time": tracker.weight_at_time,
            "date": tracker.date.strftime("%Y-%m-%d"),
            "goal": tracker.goal,
            "missing": missing,
            "consumed": consumed,
            "goal_percent": goal_percent,
            "goal_reached": goal_reached,
            "id" : tracker.id
        }
        trackers_collection.update_one({"_id": ObjectId(tracker.id)}, {"$set": tracker_data})
        return tracker_data
        
    def get_trackers(self, user_id: str) -> List[WaterTracker]:
        trackers = trackers_collection.find({"id_owner": user_id})
        if trackers is None:
            raise HTTPException(status_code=404, detail="Trackers not found")
        return self.trackers_serializer(trackers)