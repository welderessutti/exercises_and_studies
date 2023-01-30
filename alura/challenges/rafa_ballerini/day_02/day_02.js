/*
const nome = prompt("Qual o seu nome?: ");
const idade = prompt("Quantos anos você tem?: ");
const linguagem = prompt("Qual linguagem de programação você está estudando?: ");

alert(`Olá ${nome}, você tem ${idade} anos e está estudando ${linguagem}.`);
*/

function dadosPessoa() {
    const nome = document.querySelector("#nome").value;
    const idade = document.querySelector("#idade").value;
    const linguagem = document.querySelector("#linguagem").value;
    const resposta = document.querySelector(".resposta");

    resposta.innerHTML = `Olá ${nome}, você tem ${idade} anos e está estudando ${linguagem}.`;

    alert(`Olá ${nome}, você tem ${idade} anos e está estudando ${linguagem}.`);
}

const clicou = document.querySelector("#enviar");
clicou.onclick = dadosPessoa;
