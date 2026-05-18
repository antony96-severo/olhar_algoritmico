# 👁️ Olhar Algorítmico

Projeto desenvolvido para a Feira de Ciências da Escola de Tempo Integral Pastor Florêncio Nunes Neto.

O **Olhar Algorítmico** é uma aplicação web desenvolvida com Flask que utiliza Inteligência Artificial e Visão Computacional para analisar imagens capturadas pela câmera do usuário e gerar descrições automáticas em linguagem natural.

A proposta do projeto é discutir como algoritmos enxergam pessoas, objetos e contextos, promovendo reflexões sobre tecnologia, reconhecimento visual, IA e impactos sociais ligados à análise automatizada de imagens.

---

# 🚀 Tecnologias Utilizadas

- Python 3.11
- Flask
- Flask SQLAlchemy
- OpenAI API
- OpenCV
- Pillow
- HTML5
- CSS3
- JavaScript
- PostgreSQL
- Gunicorn
- Railway

---

# 🧠 Funcionalidades

- Captura de imagem pela câmera do navegador
- Envio da imagem para análise
- Geração automática de descrição usando IA
- Histórico de descrições geradas
- Interface responsiva
- Banco de dados para armazenamento das análises
- Deploy em nuvem

---

# 📸 Sobre o Projeto

O projeto busca demonstrar como sistemas de Inteligência Artificial podem interpretar imagens através de algoritmos de visão computacional.

Além da parte técnica, o sistema também propõe reflexões sobre:

- reconhecimento facial;
- vieses algorítmicos;
- racismo algorítmico;
- automação;
- impacto social da IA;
- leitura computacional da realidade.

---

# 🗂️ Estrutura do Projeto

```bash
olhar_algoritmico/
│
├── src/
│   ├── app.py
│   │
│   ├── config/
│   │   ├── database.py
│   │   └── settings.py
│   │
│   ├── controllers/
│   │   └── routes.py
│   │
│   ├── services/
│   │   ├── analisar_imagem.py
│   │   └── converter_frame.py
│   │
│   ├── templates/
│   │   ├── home.html
│   │   ├── gerar_descricao.html
│   │   └── historico.html
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   │
│   └── models/
│       └── descricao.py
│
├── requirements.txt
├── Procfile
└── README.md
```

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/olhar_algoritmico.git
```

Entre na pasta:

```bash
cd olhar_algoritmico
```

Crie a virtual environment:

```bash
python -m venv venv
```

Ative a venv:

## Windows

```bash
venv\Scripts\activate
```

## Linux/Mac

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave
SECRET_KEY=sua_chave_secreta
DATABASE_URL=sua_database_url
```

---

# ▶️ Executando o Projeto

```bash
python src/app.py
```

ou

```bash
flask run
```

---

# 🌐 Deploy

O projeto foi preparado para deploy utilizando:

- Railway
- PostgreSQL
- Gunicorn

---

# 📦 Dependências Principais

```txt
flask
flask-sqlalchemy
openai
python-dotenv
pillow
opencv-python-headless
requests
gunicorn
psycopg2-binary
```

---

# 💡 Objetivo Educacional

O sistema foi criado com fins educacionais e científicos, buscando aproximar estudantes do universo da Inteligência Artificial, da programação e da discussão ética envolvendo tecnologias emergentes.

---

# 🧑‍💻 Autor

## ANTONY DE SOUSA SEVERO

Professor e desenvolvedor back-end Python.

- GitHub: https://github.com/antony96-severo
- LinkedIn: https://www.linkedin.com/in/antony-severo-48728b290

---

# 📜 Licença

Este projeto possui finalidade educacional.
