from flask import Blueprint, request, jsonify

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    if not data or "items" not in data:
        return jsonify({"error": "No items provided"}), 400

    # Simulate order processing or forward to Stripe here
    print("Received order:", data["items"])

    # Return a dummy redirect URL (replace with Stripe/Mpesa if needed)
    return jsonify({
        "url": "https://baywoods.com/thank-you"
    }), 200
