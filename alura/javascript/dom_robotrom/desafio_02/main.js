// Sem declarar variável (não recomendável):
document.querySelector("#calcular").addEventListener("click", (evento) => {
    document.querySelector(".resultado").innerText = "<h1>Fui clicado</h1>";
});

// Declarando variável:
const escreve = document.querySelector("#calcular");
const local = document.querySelectorAll(".resultado")[1];

escreve.addEventListener("click", (evento) => {
    local.innerText = "<h2>Fui clicado</h2>";
});
