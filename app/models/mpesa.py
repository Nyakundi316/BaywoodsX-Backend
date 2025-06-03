from app.extensions import db

class MpesaTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    receipt = db.Column(db.String(50), unique=True)
    result = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
