from fastapi import FastAPI, Form
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.middleware.cors import CORSMiddleware
from src.controllers import user_controller, water_tracker_controller
from fastapi.openapi.utils import get_openapi
from src.app import frontend_app
import uvicorn

api = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:443",
    "https://localhost",
    "https://localhost:8000",
    "https://localhost:443",
    "https://drink-water-tracker-kvgl74sgpa-rj.a.run.app",
    "https://drink-water-tracker-kvgl74sgpa-rj.a.run.app:8000",
    "http://drink-water-tracker-kvgl74sgpa-rj.a.run.app"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.mount("/app", WSGIMiddleware(frontend_app))

@api.get("/")
def hello_world():
    return {"Hello": "World"}

api.include_router(user_controller.router)
api.include_router(water_tracker_controller.router)

class DocsSchema:
    def info_docs():
        if api.openapi_schema:
            return api.openapi_schema
        openapi_schema = get_openapi(
            title="Drink Water Tracker API",
            version="1.0",
            routes=api.routes,
        )
        openapi_schema["info"] = {
            "title": "Drink Water Tracker API",
            "version": "1.0",
            "description": "A simple API with MongoDB to track your daily water intake.",
            "contact": {
                "name": "Gabriel Coelho",
                "url": "gabrielfmcoelho.github.io",
                "email": "gabrielcoelho09gc@gmail.com"
            }
        }
        api.openapi_schema = openapi_schema
        return api.openapi_schema
    
    def get_docs():
        return DocsSchema.info_docs()

if __name__ == "__main__": 
    uvicorn.run(api,
                host="0.0.0.0",
                port=8000,
                reload=True)