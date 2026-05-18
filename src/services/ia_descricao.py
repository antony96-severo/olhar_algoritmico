from openai import OpenAI

from src.config.settings import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


def gerar_descricao_imagem(imagem_base64):
    if not imagem_base64:
        return None

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": """
Analise a imagem enviada e organize a resposta nas seguintes categorias:

1. Descrição geral:
Faça uma descrição objetiva da cena, da pessoa e dos elementos visíveis.

2. Características visuais:
Descreva detalhes como:
- cabelo
- roupas
- acessórios
- expressão facial
- postura
- estilo visual

3. Adjetivos descritivos:
Liste adjetivos coerentes com a aparência visual observada.

4. Inferências possíveis:
Faça inferências moderadas e hipotéticas sobre:
- hobbies
- gostos musicais
- profissão
- estética predominante

Deixe claro que são hipóteses.

5. Termos subjetivos:
Apresente palavras ou expressões subjetivas relacionadas à atmosfera da imagem.

6. Traços fenotípicos visíveis:
Descreva apenas características físicas observáveis, como:
- tonalidade de pele
- textura e cor do cabelo
- traços faciais
- características gerais visíveis

Importante:
- Diferencie descrição visual de inferência.
- Não apresente hipóteses como certezas.
- A resposta deve ser clara, organizada e em português.
"""
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{imagem_base64}"
                    }
                ]
            }
        ]
    )

    return response.output_text
