from app.extensions import db

class MenRunnerProduct(db.Model):
    __tablename__ = 'men_runner_products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(100))
    type = db.Column(db.String(100))
    images = db.relationship('MenRunnerImage', backref='product', cascade='all, delete-orphan')

class MenRunnerImage(db.Model):
    __tablename__ = 'men_runner_images'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    product_id = db.Column(db.Integer, db.ForeignKey('men_runner_products.id'))