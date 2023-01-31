const trocaTexto = document.getElementById("texto")

trocaTexto.addEventListener("mouseenter", mudar)
trocaTexto.addEventListener("mouseout", voltar)

function mudar() {
    trocaTexto.innerText = "Hello, World!"
}

function voltar() {
    trocaTexto.innerText = "O inverno está chegando"
}