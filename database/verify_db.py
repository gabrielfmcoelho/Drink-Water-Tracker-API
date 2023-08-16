
from pymongo import MongoClient

def verify_db_connection(URI = "45.79.205.185:27017"):
    try:
        client_test = MongoClient(URI)
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
    verify_db_connection()
    exit(1)