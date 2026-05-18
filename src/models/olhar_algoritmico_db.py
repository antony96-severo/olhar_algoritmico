from datetime import datetime, UTC
from src.config.database import db


class DescricaoImagem(db.Model):
    __tablename__ = "descricoes_imagens"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)
    raca = db.Column(db.String(100), nullable=False)
    descricao_completa = db.Column(db.Text, nullable=False)

    criado_em = db.Column(
        db.DateTime,
        default=lambda: datetime.now(UTC)
    )