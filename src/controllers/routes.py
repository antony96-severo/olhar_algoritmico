from flask import jsonify, render_template, request

from src.models.olhar_algoritmico_db import DescricaoImagem
from src.services.ia_descricao import gerar_descricao_imagem
from src.services.salvar_descricao import salvar_descricao


def registrar_rotas(app):

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/descrever-imagem", methods=["GET"])
    def descrever_imagem():
        return render_template("descrever_imagem.html")

    @app.route("/api/descrever-imagem", methods=["POST"])
    def api_descrever_imagem():
        dados = request.get_json(silent=True)

        if not dados:
            return jsonify({"erro": "Nenhum dado foi enviado."}), 400

        nome = dados.get("nome")
        raca = dados.get("raca")
        imagem_base64 = dados.get("imagem_base64")

        if not nome or not raca or not imagem_base64:
            return jsonify({"erro": "Nome, raça/cor e imagem são obrigatórios."}), 400

        descricao = gerar_descricao_imagem(imagem_base64)

        if descricao is None:
            return jsonify({"erro": "Não foi possível gerar a descrição da imagem."}), 500

        descricao_salva = salvar_descricao(
            nome=nome,
            raca=raca,
            descricao_completa=descricao
        )

        return jsonify({
            "id": descricao_salva.id,
            "nome": descricao_salva.nome,
            "raca": descricao_salva.raca,
            "descricao": descricao_salva.descricao_completa
        })

    @app.route("/historico")
    def historico():
        descricoes = DescricaoImagem.query.order_by(
            DescricaoImagem.criado_em.desc()
        ).all()

        return render_template(
            "historico.html",
            descricoes=descricoes
        )
