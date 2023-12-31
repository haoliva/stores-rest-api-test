from app import app
from db import db

db.init_app(app)


with app.app_context():
    def create_tables():
        db.create_all()
