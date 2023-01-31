const listaDeTintas = document.querySelector(".lista");
const botaoLimpaLista = document.querySelector("#botao-limpa");
const botaoInsereLista = document.querySelector("#botao-insere");

function fazAparecer() {
    listaDeTintas.style.display = "block";
}

function fazDesaparecer() {
    listaDeTintas.style.display = "none";
}

botaoLimpaLista.addEventListener("click", () => {
    fazDesaparecer();
})

botaoInsereLista.addEventListener("click", () => {
    fazAparecer();
})
