from flask import Flask
from app.main.routes.tag_routes import tags_routes_bp

app = Flask(__name__)

app.register_blueprint(tags_routes_bp)