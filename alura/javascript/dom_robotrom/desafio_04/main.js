// Cria um array de backup contendo o texto de cada "li .item".
function criaListaBackup() {
    for (let c = 0; c < listaDeTintas.length; c++) {
        console.log(listaDeTintasBackup);
        listaDeTintasBackup.push(listaDeTintas[c].innerText);
    }
}

// Insere em cada "li .item" a string do array "listaDeTintasBackup.
function insereItens() {
    for (let c = 0; c < listaDeTintas.length; c++) {
        listaDeTintas[c].innerText = listaDeTintasBackup[c];
    }
}

// Remove todos os textos de cada "li .item".
function removeItens() {
    for (let c = 0; c < listaDeTintas.length; c++) {
        listaDeTintas[c].innerText = "";
    }
}

const botaoLimpaLista = document.querySelector("#botao-limpa");
const botaoInsereLista = document.querySelector("#botao-insere");

const listaDeTintas = document.querySelectorAll(".item");
const listaDeTintasBackup = [];

botaoLimpaLista.addEventListener("click", () => {
    removeItens();
})

botaoInsereLista.addEventListener("click", () => {
    insereItens();
})

// Executa a função "criaListaBackup" assim que o HTML é carregado.
window.onload = criaListaBackup;
