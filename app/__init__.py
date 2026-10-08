from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from app.settings import Settings

app = Flask(__name__)
app.config.from_object(Settings)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from .models import Usuario

@login_manager.user_loader
def load_user(id: int | str) -> Usuario | None:
    return db.session.get(Usuario, int(id))

from . import models, routes 

