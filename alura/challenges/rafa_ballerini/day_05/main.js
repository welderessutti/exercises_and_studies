const resultado = document.getElementById("resultado");
let listaDeCompras = {};

while (true) {
    let incluir = prompt("Deseja incluir um item [S/N]?:");
    
    if (incluir == "S") {
        let item = prompt("Qual é o item?:");
        let categoria = prompt("Qual a categoria do item?:");

        if (categoria in listaDeCompras) {
            listaDeCompras[categoria].push(item);
        } else {
            listaDeCompras[categoria] = [item];
        }
    } else {
        break;
    }
}

for (elemento of Object.keys(listaDeCompras)) {
    resultado.innerHTML += `${elemento}: `;

    for (item of listaDeCompras[elemento]) {
        resultado.innerHTML += `${item} `;
    }
    resultado.innerHTML += `<br>`;
}
