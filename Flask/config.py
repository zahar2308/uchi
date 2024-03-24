import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

