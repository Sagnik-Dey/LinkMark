from flask import Flask
from dotenv import load_dotenv
import sys
import os

sys.path.append("app")
from landing import landing_bp
from login import login_bp
from register import register_bp
from home import home_bp
from add import add_bp
from view import view_bp
from delete import delete_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    app.secret_key = os.getenv("SECRET_KEY")
    
    app.register_blueprint(landing_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(add_bp)
    app.register_blueprint(view_bp)
    app.register_blueprint(delete_bp)
    
    return app