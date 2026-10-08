from dotenv import load_dotenv

import os


load_dotenv()

class Settings:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///sqlite3.db')

