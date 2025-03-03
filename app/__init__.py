from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Load configuration
    app.config.from_object('config.Config')
    
    # Initialize database
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register routes
    from app.routes.weather import bp as weather_bp
    from app.routes.crops import bp as crops_bp
    from app.routes.iot import bp as iot_bp
    from app.routes.blockchain import bp as blockchain_bp
    
    app.register_blueprint(weather_bp)
    app.register_blueprint(crops_bp)
    app.register_blueprint(iot_bp)
    app.register_blueprint(blockchain_bp)
    
    return app
