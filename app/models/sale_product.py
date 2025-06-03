# app/models/sale_product.py
from app.extensions import db

class SaleProduct(db.Model):
    __tablename__ = "sale_products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    discount = db.Column(db.Integer, nullable=True)
    colors = db.Column(db.JSON, nullable=False)  # ✅ This replaces 'images'
    color = db.Column(db.String(50), nullable=True)
    sizes = db.Column(db.JSON, nullable=True)
