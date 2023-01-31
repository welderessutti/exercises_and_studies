function manipulandoDados(operacao, controle) {
    const peca = controle.querySelector("[data-contador]");

    if (operacao === "-") {
        peca.value = parseInt(peca.value) - 1;
    } else {
        peca.value = parseInt(peca.value) + 1;
    }
}

const controle = document.querySelectorAll("[data-controle]");

controle.forEach( (elemento) => {
    elemento.addEventListener("click", (evento) => {
        manipulandoDados(evento.target.dataset.controle, evento.target.parentNode);
    });
});
