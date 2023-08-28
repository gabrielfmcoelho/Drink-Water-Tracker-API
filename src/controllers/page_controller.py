from flask import Blueprint, render_template
from datetime import date
import requests
from database.schemas.user_schema import UserSchema
from database.schemas.water_tracker_schema import WaterTrackerSchema
from database.verify_db import verify_db_connection

user_schema = UserSchema()
water_tracker_schema = WaterTrackerSchema()

page_blueprint = Blueprint('page', __name__)

def get_user_from_api(user_id):
    try:
        user_response = requests.get(f"/user/{user_id}/")
        return user_response.json()
    except Exception as e:
        print(e)
        return None

def get_tracker_from_api(user_id, tracker_date=None):
    try:
        if tracker_date is None:
            tracker_date = date.today().strftime("%Y-%m-%d")
            tracker_response = requests.get(f"/user/{user_id}/tracker/")
        else:
            tracker_response = requests.get(f"/user/{user_id}/tracker/{tracker_date}/")
        return tracker_response.json()
    except Exception as e:
        print(e)
        return None

def get_history_from_api(user_id):
    try:
        history_response = requests.get(f"/user/{user_id}/history/")
        return history_response.json()
    except Exception as e:
        print(e)
        return []

def assure_db_connection():
    status = verify_db_connection()
    if not status:
        return render_template("error.html", message="Error connecting to database")

@page_blueprint.route("/")
def home_page():
    #assure_db_connection()
    return render_template("home_page.html")

@page_blueprint.route("/error")
def error_page():
    return render_template("error.html")

@page_blueprint.route("/<user_id>/tracker/<tracker_date>")
def user_tracker_page(user_id, tracker_date=None):
    #assure_db_connection()
    try:
        tracker = get_tracker_from_api(user_id, tracker_date)
        user = get_user_from_api(user_id)
    except Exception as e:
        print(e)
        return render_template("error.html", message="Error connecting to API")
    
    return render_template("tracker.html", user=user, date=tracker['date'], entry=tracker)

@page_blueprint.route("/<user_id>/tracker/")
def _(user_id):
    return user_tracker_page(user_id, None)

@page_blueprint.route("/<user_id>/history/")
def user_history_page(user_id):
    #assure_db_connection()
    try:
        trackers = get_history_from_api(user_id)
        user = get_user_from_api(user_id)
    except Exception as e:
        print(e)
        return render_template("error.html", message="Error connecting to API")
    
    return render_template("history.html", user=user, entries=trackers)