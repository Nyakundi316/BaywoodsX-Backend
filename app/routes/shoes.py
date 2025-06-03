from flask import Blueprint, request, jsonify
from app.models.shoes_product import ShoesProduct, ShoesProductImage
from extensions import db

shoes_bp = Blueprint("shoes_products", __name__, url_prefix="/api/shoesproducts")

# ✅ Get all shoes products
@shoes_bp.route("/", methods=["GET"])
def get_all_shoes_products():
    products = ShoesProduct.query.all()
    return jsonify([product.to_dict() for product in products]), 200

# ✅ Get one shoe product by ID
@shoes_bp.route("/<int:product_id>", methods=["GET"])
def get_shoe_product(product_id):
    product = ShoesProduct.query.get_or_404(product_id)
    return jsonify(product.to_dict()), 200

# ✅ Create a new shoe product (admin-level)
@shoes_bp.route("/", methods=["POST"])
def create_shoe_product():
    data = request.get_json()
    product = ShoesProduct(
        name=data.get("name"),
        category=data.get("category"),
        price=data.get("price"),
        sizes=data.get("sizes", [])
    )
    db.session.add(product)
    db.session.commit()

    # Optional: Add images
    images = data.get("images", [])
    for img_url in images:
        image = ShoesProductImage(url=img_url, product_id=product.id)
        db.session.add(image)
    db.session.commit()

    return jsonify(product.to_dict()), 201

# ✅ Update a shoe product
@shoes_bp.route("/<int:product_id>", methods=["PUT"])
def update_shoe_product(product_id):
    product = ShoesProduct.query.get_or_404(product_id)
    data = request.get_json()

    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.price = data.get("price", product.price)
    product.sizes = data.get("sizes", product.sizes)

    db.session.commit()

    return jsonify(product.to_dict()), 200

# ✅ Delete a shoe product
@shoes_bp.route("/<int:product_id>", methods=["DELETE"])
def delete_shoe_product(product_id):
    product = ShoesProduct.query.get_or_404(product_id)

    # Delete associated images first
    ShoesProductImage.query.filter_by(product_id=product.id).delete()

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"}), 200

# ✅ Filter by brand
@shoes_bp.route("/brand/<string:brand_name>", methods=["GET"])
def get_shoes_by_brand(brand_name):
    products = ShoesProduct.query.filter_by(brand=brand_name).all()
    return jsonify([product.to_dict() for product in products]), 200
