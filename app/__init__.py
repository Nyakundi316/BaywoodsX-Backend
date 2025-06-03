from flask import Flask
from app.extensions import db, jwt, migrate
from app.routes.auth import auth_bp
from app.routes.products import products_bp
from app.routes.cart import cart_bp
from app.routes.mpesa import mpesa_bp
from app.routes.sale import sale_bp  # ✅ Add this line
from app.models import user, product  # ✅ Import models so Flask is aware
from app.models.mpesa import MpesaTransaction
from flask_cors import CORS
from app.models.sale_product import SaleProduct
from app.models.men_runner import MenRunnerProduct, MenRunnerImage

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.AppConfig")
    CORS(app)
    
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(products_bp, url_prefix="/api")
    app.register_blueprint(cart_bp, url_prefix="/api")
    app.register_blueprint(mpesa_bp, url_prefix="/api")
    app.register_blueprint(sale_bp, url_prefix="/api")  # ✅ Corrected and namespaced

    return app
