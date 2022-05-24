# Model a many-to-many relationship between an orders table and a products 
# table such that a single order can have many products and a product can be associated with many orders.

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    order_product = db.relationship('Orders_Products', backref='orderbr') 

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    order_product = db.relationship('Orders_Products', backref='productsbr') 

class Orders_Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column('orders_id', db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column('products_id', db.Integer, db.ForeignKey('products.id'))

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')
