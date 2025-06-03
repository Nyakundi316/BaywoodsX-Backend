from flask import Blueprint, request, jsonify
from app.models.sale_product import SaleProduct
from app.extensions import db

sale_bp = Blueprint("sale", __name__)

# GET /api/sale-products
@sale_bp.route("/sale-products", methods=["GET"])
def get_sale_products():
    category = request.args.get("category")
    query = SaleProduct.query

    if category:
        query = query.filter_by(category=category)

    sale_products = query.all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price,
            "discount": p.discount,
            "colors": p.colors,       # ✅ use 'colors' instead of 'images'
            "color": p.color,
            "sizes": p.sizes
        } for p in sale_products
    ])
