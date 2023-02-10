const comecar = document.getElementById("comecar");
const num_pc = getRandomInt(1, 10);

comecar.addEventListener("click", () => {
    tentativas();
})

function tentativas() {
    let cont = 1;
    const total = 3;
    while (cont <= total) {
        let tentativa = prompt(`${cont}ª tentativa:`);

        if (tentativa == num_pc) {
            alert("Parabéns! Você acertou.");
            break;
        } else {
            if (cont < 3) {
                alert(`Você errou. Você tem mais ${total - cont} tentativas.`);
            } else {
                alert("Você perdeu!");
            }
        }
        cont++;
    }
}

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min);
  }
  