import base64, requests
from flask import Blueprint, request, jsonify
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

mpesa_bp = Blueprint("mpesa", __name__)

# Get access token
def get_access_token():
    consumer_key = os.getenv("MPESA_CONSUMER_KEY")
    consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    res = requests.get(url, auth=(consumer_key, consumer_secret))
    return res.json().get("access_token")

# Format password for STK Push
def generate_password():
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortcode = os.getenv("MPESA_SHORTCODE")
    passkey = os.getenv("MPESA_PASSKEY")
    data = shortcode + passkey + timestamp
    password = base64.b64encode(data.encode()).decode()
    return password, timestamp

@mpesa_bp.route("/mpesa/checkout", methods=["POST"])
def initiate_stk_push():
    data = request.get_json()
    phone = data.get("phone")
    amount = int(data.get("amount", 1))

    token = get_access_token()
    password, timestamp = generate_password()

    payload = {
        "BusinessShortCode": os.getenv("MPESA_SHORTCODE"),
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": os.getenv("MPESA_SHORTCODE"),
        "PhoneNumber": phone,
        "CallBackURL": os.getenv("MPESA_CALLBACK_URL"),
        "AccountReference": "Baywoods",
        "TransactionDesc": "Baywoods Order"
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    res = requests.post("https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest", json=payload, headers=headers)
    return jsonify(res.json())
