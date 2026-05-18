from src.config.database import db
from src.models.olhar_algoritmico_db import DescricaoImagem


def salvar_descricao(nome, raca, descricao_completa):
    nova_descricao = DescricaoImagem(
        nome=nome,
        raca=raca,
        descricao_completa=descricao_completa
    )

    db.session.add(nova_descricao)
    db.session.commit()

    return nova_descricao