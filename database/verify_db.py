
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

def verify_db_connection(uri):
    try:
        client_test = MongoClient(uri)
        server_info = client_test.server_info()
        print("Connected to MongoDB")
        print(f"Server version: {server_info['version']}")
        print(f"Server status: {server_info['ok']}")
        status = True
    except Exception as e:
        print("Could not connect to MongoDB")
        print(e)
        status = False
    finally:
        client_test.close()
    
    return status

if __name__ == "__main__":
    verify_db_connection(MONGODB_URI)
    exit(1)