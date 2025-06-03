from app.extensions import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=True)  # ✅ Required
    price = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(255), nullable=False)
    sizes = db.Column(db.PickleType, nullable=True)  # ✅ List of sizes

