from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from app.extensions import db, jwt, migrate
from app.routes.auth import auth_bp
from app.routes.products import products_bp
from app.models.user import User
from app.models.product import Product
from app.routes.sale import sale_bp
from app.routes.shoes import shoes_bp
from app.routes.men_runner import men_runners_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)  # ✅ Correct use of class reference

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(shoes_bp)
    app.register_blueprint(men_runners_bp)
    app.register_blueprint(sale_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(products_bp, url_prefix="/api")

    # ✅ Only use create_all() if not using flask-migrate
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    with app.app_context():
        
        print("🔍 Registered routes:")
        for rule in app.url_map.iter_rules():
            print(rule)

