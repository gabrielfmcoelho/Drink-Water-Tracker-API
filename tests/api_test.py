# test_app.py
from datetime import datetime
from fastapi.testclient import TestClient
import pytest
from src.models.water_tracker import WaterTracker
from app import api
from src.models.user import CreateUser, User
from datetime import timedelta

## new tests
client = TestClient(api)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}

sample_user_to_create = CreateUser(name="John Doe", weight=65)
user_created = None
tracker_created = None

def test_create_user():
    response = client.post("/user/", json=sample_user_to_create.dict())
    response_user = response.json()
    assert "id" in response_user
    global user_created 
    user_created = User(**response_user)

def test_get_user():
    global user_created 
    valid_user_id = user_created.id
    response = client.get(f"/user/{valid_user_id}/")
    assert response.status_code == 200

def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_today_tracker():
    global user_created, tracker_created
    valid_user_id = user_created.id
    response = client.get(f"/user/{valid_user_id}/tracker/")
    assert response.status_code == 200
    response_tracker = response.json()
    assert "id_owner" in response_tracker
    tracker_created = WaterTracker(**response_tracker)

def test_get_tracker():
    global user_created, tracker_created
    valid_user_id = user_created.id
    valid_tracker_date = tracker_created.date
    response = client.get(f"/user/{valid_user_id}/tracker/{valid_tracker_date}/")
    assert response.status_code == 200
    assert "id_owner" in response.json()

def test_update_tracker():
    global user_created, tracker_created
    valid_user_id = user_created.id
    valid_tracker_date = tracker_created.date
    update_data = {"cupsize": 2000}
    response = client.put(f"/user/{valid_user_id}/tracker/{valid_tracker_date}/", json=update_data)
    assert response.status_code == 200
    assert "id_owner" in response.json()

def test_create_specific_tracker():
    global user_created, tracker_created
    valid_user_id = user_created.id
    valid_tracker_date = tracker_created.date - timedelta(days=1)
    response = client.post(f"/user/{valid_user_id}/tracker/{valid_tracker_date}/")
    assert response.status_code == 200
    assert "id_owner" in response.json()

def test_list_trackers():
    global user_created
    valid_user_id = user_created.id
    response = client.get(f"/user/{valid_user_id}/history/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
if __name__ == "__main__":
    pytest.main()
