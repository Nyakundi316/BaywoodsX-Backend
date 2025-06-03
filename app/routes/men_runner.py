# routes/men_runners.py
from flask import Blueprint, jsonify
from app.models.men_runner import MenRunnerProduct

men_runners_bp = Blueprint("men_runners", __name__)

@men_runners_bp.route('/api/men-runners', methods=['GET'], endpoint='get_men_runners')
def get_men_runners():
    products = MenRunnerProduct.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "brand": p.brand,
            "category": p.category,
            "type": p.type,
            "price": float(p.price),
            "sizes": p.sizes,
            "image": p.images[0].url if p.images else None
        } for p in products
    ])
