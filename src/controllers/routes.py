from flask import render_template, request
from src.models.olhar_algoritmico_db import DescricaoImagem
from src.services.ia_descricao import gerar_descricao_imagem
from src.services.salvar_descricao import salvar_descricao


def registrar_rotas(app):

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/descrever-imagem", methods=["GET", "POST"])
    def descrever_imagem():
        if request.method == "GET":
            return render_template("descrever_imagem.html")

        nome = request.form.get("nome")
        raca = request.form.get("raca")

        descricao = gerar_descricao_imagem()

        if descricao is None:
            return render_template(
                "descrever_imagem.html",
                erro="Não foi possível capturar a imagem."
            )

        descricao_salva = salvar_descricao(
            nome=nome,
            raca=raca,
            descricao_completa=descricao
        )

        return render_template(
            "descrever_imagem.html",
            nome=nome,
            raca=raca,
            descricao=descricao_salva.descricao_completa
        )

    @app.route("/historico")
    def historico():
        descricoes = DescricaoImagem.query.order_by(
            DescricaoImagem.criado_em.desc()
        ).all()

        return render_template(
            "historico.html",
            descricoes=descricoes
        )