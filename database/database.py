from pymongo import MongoClient
from config.settings import MONGODB_URI

try:
    client = MongoClient(MONGODB_URI)
    server_info = client.server_info()
    print("Connected to MongoDB")
    print(f"Server version: {server_info['version']}")
    print(f"Server status: {server_info['ok']}")
except Exception as e:
    print("Could not connect to MongoDB")
    print(e)
    exit(1)
db = client["water_tracker"]
users_collection = db["users"]
trackers_collection = db["trackers"]