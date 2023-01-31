function manipulandoDados(operacao) {
    if (operacao === "-") {
        braco.value = parseInt(braco.value) - 1;
    } else {
        braco.value = parseInt(braco.value) + 1;
    }
}

const subtrair = document.querySelector("#subtrair");
const somar = document.querySelector("#somar");
const braco = document.querySelector("#braco");
const controle = document.querySelectorAll(".controle-ajuste");

/*
somar.addEventListener("click", (evento) => {  // Arrow Function ou Função Anônima.
    braco.value = parseInt(braco.value) + 1;
});

subtrair.addEventListener("click", (evento) => {  // Arrow Function ou Função Anônima.
    braco.value = parseInt(braco.value) - 1;
});
*/
controle.forEach( (elemento) => {
    elemento.addEventListener("click", (evento) => {
        manipulandoDados(evento.target.textContent);
    });
});
