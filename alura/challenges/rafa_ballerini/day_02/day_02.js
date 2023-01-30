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
    const msg = `Olá ${nome}, você tem ${idade} anos e está estudando ${linguagem}.`;

    resposta.innerHTML = msg;

    alert(msg);

    gostaDeEstudar(linguagem);
}

function gostaDeEstudar(texto) {
    const resposta_01 = prompt(`Você gosta de estudar ${texto}? Responda 1 para SIM ou 2 para NÃO.`);

    if (resposta_01 == 1) {
        alert("Muito bom! Continue estudando e você terá muito sucesso.");
    } else if (resposta_01 == 2) {
        alert("Ahh que pena... Já tentou aprender outras liguagens?");
    } else {
        alert("Resposta inválida!");
    }
}

const clicou = document.querySelector("#enviar");
clicou.onclick = dadosPessoa;
