# models/shoes_product.py
from app.extensions import db
from sqlalchemy.dialects.sqlite import JSON

class ShoesProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('shoes_product.id'), nullable=False)

class ShoesProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(50), nullable=True)
    sizes = db.Column(db.JSON, default=[])
    
    # ✅ This works now because ShoesProductImage is already defined
    images = db.relationship('ShoesProductImage', backref='product', lazy=True)



    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "category": self.category,
            "price": self.price,
            "sizes": self.sizes,
            "images": [img.url for img in self.images]
        }
