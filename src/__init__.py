from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from src import models
from src import controllers
from src import database
from src.routes import initalize_routes

initalize_routes()
