from flask import session, redirect, request, render_template
from p4_pkg import app, db
from p4_pkg.models import db, User, Meal, Category, Order, meals_orders_association

@app.route('/')
def main():
    output = render_template('index.html')
    return output