from flask import Flask
from p4_pkg.config import Config
from p4_pkg.models import db, User, Meal, Category, Order, meals_orders_association

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

from p4_pkg.views import *