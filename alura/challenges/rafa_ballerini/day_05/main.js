const resultado = document.getElementById("resultado");
let listaDeCompras = {};

while (true) {
    let incluir = prompt("Deseja incluir um item [s/n]?:");
    
    if (incluir == "s") {
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
        if (item == listaDeCompras[elemento][listaDeCompras[elemento].length - 1]) {
            resultado.innerHTML += `${item}.`;
        } else {
            resultado.innerHTML += `${item}, `;
        }
    }
    resultado.innerHTML += `<br>`;
}
