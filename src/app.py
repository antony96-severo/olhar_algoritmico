import os
from flask import Flask
from src.config.database import db
from src.controllers.routes import registrar_rotas

app = Flask(__name__)

database_url = os.getenv(
    "DATABASE_URL",
    "sqlite:///olhar_algoritmico.db"
)

if database_url.startswith("postgres://"):
    database_url = database_url.replace(
        "postgres://",
        "postgresql://",
        1
    )

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

registrar_rotas(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)