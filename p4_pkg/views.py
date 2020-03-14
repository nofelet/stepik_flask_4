from flask import session, redirect, request, render_template
from p4_pkg import app, db
from p4_pkg.models import db, User, Meal, Category, Order, meals_orders_association

@app.route('/')
def main():
    number = 6
    cost = 488
    output = render_template('index.html',
                             number=number,
                             cost=cost)
    return output