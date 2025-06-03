from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.extensions import db

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    brand = request.args.get("brand")
    query = Product.query

    if category:
        query = query.filter_by(category=category)
    if brand:
        query = query.filter_by(brand=brand)

    products = query.all()

    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "brand": p.brand,
            "category": p.category,
            "price": p.price,
            "image": p.image,
            "color": p.color,
            "sizes": p.sizes
        } for p in products
    ])
@products_bp.route("/brands", methods=["GET"])
def get_all_brands():
    brands = db.session.query(Product.brand).distinct().all()
    return jsonify([b[0] for b in brands])
@products_bp.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        "id": product.id,
        "name": product.name,
        "brand": product.brand,
        "category": product.category,
        "price": product.price,
        "image": product.image,
        "color": product.color,
        "sizes": product.sizes
    })
@products_bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data["name"],
        brand=data.get("brand"),
        category=data["category"],
        price=data["price"],
        image=data["image"],
        color=data.get("color"),
        sizes=data.get("sizes", [])
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created", "id": new_product.id}), 201

@products_bp.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    for key in ["name", "brand", "category", "price", "image", "color", "sizes"]:
        if key in data:
            setattr(product, key, data[key])
    db.session.commit()
    return jsonify({"message": "Product updated"})

@products_bp.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})
