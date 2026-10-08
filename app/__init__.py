from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models, routes 

