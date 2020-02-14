import os

current_path = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join("sqlite:///", current_path, "w5.db")

class Config:
    DEBUG = True
    SECRET_KEY = 'very_secret_phrase'
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False