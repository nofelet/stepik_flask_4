from flask import Flask

from models import db, User, Group, Applicant
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)