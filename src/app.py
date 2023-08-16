from flask import Flask
from src.controllers.page_controller import page_blueprint

frontend_app = Flask(__name__,
                     static_folder="./views/static",
                     template_folder="./views/templates")

frontend_app.register_blueprint(page_blueprint)

