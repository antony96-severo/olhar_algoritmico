import os
from flask import Flask
from src.config.database import db
from src.controllers.routes import registrar_rotas


def create_app():
    app = Flask(__name__)
    
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
database_url = os.getenv("DATABASE_URL")

if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///olhar_algoritmico.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    registrar_rotas(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
