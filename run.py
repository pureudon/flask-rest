from app import app
from db import db

print("hihi app is running")
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()