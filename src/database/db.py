from src import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATION_DIR = os.path.join('src', 'database', 'migrations')

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)
