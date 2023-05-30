async function cep() {
    var consultaCep = await fetch("./meu_arquivo.json");
    var consultaCepConvertida = await consultaCep.json();

    console.log(consultaCepConvertida);

    var paragrafo = document.getElementById("escreve");

    for (const [key, value] of Object.entries(consultaCepConvertida)) {
        paragrafo.innerHTML += `<p>${key}: ${value}</p>`;
    }
}

cep();
