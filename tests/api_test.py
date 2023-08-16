# test_app.py
from datetime import datetime
from fastapi.testclient import TestClient
import pytest
from app import api 
from src.models.user import CreateUser, User
from src.models.water_tracker import WaterTracker
from bson import ObjectId

client = TestClient(api)

sample_user = CreateUser(name="John Doe", weight=70)

def test_create_user():
    response = client.post("/user/", json=sample_user.dict())
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == sample_user.name
    assert data["weight"] == sample_user.weight

def test_get_user():
    create_response = client.post("/user/", json=sample_user.dict())
    user_id = create_response.json()["id"]

    response = client.get(f"/user/{user_id}/")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == sample_user.name
    assert data["weight"] == sample_user.weight

def test_create_specific_tracker():
    create_response = client.post("/user/", json=sample_user.dict())
    user_id = create_response.json()["id"]

    response = client.post(f"/user/{user_id}/tracker/{datetime.now().date().strftime('%Y-%m-%d')}/")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id_owner"] == user_id

def test_tracker_update_consume():
    create_user_response = client.post("/user/", json=sample_user.dict())
    user_id = create_user_response.json()["id"]
    create_tracker_response = client.post(f"/user/{user_id}/tracker/{datetime.now().date().strftime('%Y-%m-%d')}/")
    tracker_id = create_tracker_response.json()["id"]

    update_data = {"cupsize": 250}
    response = client.put(f"/user/{user_id}/tracker/{tracker_id}/", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["consumed"] == update_data["cupsize"]

if __name__ == "__main__":
    pytest.main()
