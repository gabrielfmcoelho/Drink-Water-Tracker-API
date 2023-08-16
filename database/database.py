from pymongo import MongoClient
from config.settings import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client["water_tracker"]
users_collection = db["users"]
trackers_collection = db["trackers"]