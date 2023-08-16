from fastapi import FastAPI, Form
from fastapi.middleware.wsgi import WSGIMiddleware
from src.controllers import user_controller, water_tracker_controller
from src.app import frontend_app
import uvicorn

api = FastAPI()

api.mount("/app", WSGIMiddleware(frontend_app))

@api.get("/")
def hello_world():
    return {"Hello": "World"}

api.include_router(user_controller.router)
api.include_router(water_tracker_controller.router)

if __name__ == "__main__": 
    uvicorn.run(api,
                host="0.0.0.0",
                port=8000,
                debug=True,
                reload=True)