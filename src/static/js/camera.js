const video = document.getElementById("camera");
const canvas = document.getElementById("canvas");
const form = document.getElementById("form-descricao");
const botaoGerar = document.getElementById("botao-gerar");
const mensagemErro = document.getElementById("mensagem-erro");
const mensagemCarregando = document.getElementById("mensagem-carregando");
const resultado = document.getElementById("resultado");
const resultadoNome = document.getElementById("resultado-nome");
const resultadoRaca = document.getElementById("resultado-raca");
const resultadoDescricao = document.getElementById("resultado-descricao");

async function iniciarCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: false
        });

        video.srcObject = stream;
    } catch (erro) {
        mostrarErro("Não foi possível acessar a câmera. Verifique a permissão do navegador.");
    }
}

function capturarImagemBase64() {
    const largura = video.videoWidth;
    const altura = video.videoHeight;

    if (!largura || !altura) {
        return null;
    }

    canvas.width = largura;
    canvas.height = altura;

    const contexto = canvas.getContext("2d");
    contexto.drawImage(video, 0, 0, largura, altura);

    const imagemCompleta = canvas.toDataURL("image/jpeg", 0.9);
    return imagemCompleta.replace("data:image/jpeg;base64,", "");
}

function mostrarErro(texto) {
    mensagemErro.textContent = texto;
    mensagemErro.classList.remove("hidden");
}

function limparErro() {
    mensagemErro.textContent = "";
    mensagemErro.classList.add("hidden");
}

function controlarCarregamento(estaCarregando) {
    if (estaCarregando) {
        mensagemCarregando.classList.remove("hidden");
        botaoGerar.disabled = true;
        botaoGerar.textContent = "Gerando...";
    } else {
        mensagemCarregando.classList.add("hidden");
        botaoGerar.disabled = false;
        botaoGerar.textContent = "Gerar descrição";
    }
}

form.addEventListener("submit", async function (evento) {
    evento.preventDefault();
    limparErro();
    resultado.classList.add("hidden");

    const nome = document.getElementById("nome").value.trim();
    const raca = document.getElementById("raca").value;
    const imagemBase64 = capturarImagemBase64();

    if (!nome || !raca) {
        mostrarErro("Preencha nome e raça/cor declarada.");
        return;
    }

    if (!imagemBase64) {
        mostrarErro("A câmera ainda não está pronta. Aguarde alguns segundos e tente novamente.");
        return;
    }

    controlarCarregamento(true);

    try {
        const resposta = await fetch("/api/descrever-imagem", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                nome: nome,
                raca: raca,
                imagem_base64: imagemBase64
            })
        });

        const dados = await resposta.json();

        if (!resposta.ok) {
            mostrarErro(dados.erro || "Erro ao gerar descrição.");
            return;
        }

        resultadoNome.textContent = dados.nome;
        resultadoRaca.textContent = dados.raca;
        resultadoDescricao.textContent = dados.descricao;
        resultado.classList.remove("hidden");
    } catch (erro) {
        mostrarErro("Erro de comunicação com o servidor.");
    } finally {
        controlarCarregamento(false);
    }
});

iniciarCamera();
