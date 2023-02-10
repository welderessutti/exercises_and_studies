const first = prompt("Você quer seguir para área de Front-End ou Back-End?");

if (first == "Front-End") {
    const front = prompt("Você quer aprender React ou Vue?");

    const especial = prompt(`Você quer se especializar na área de ${front} ou se desenvolver para Fullstack?`);

    if (especial == front) {
        alert(`A área de ${especial} é muito legal!`);

        let continuar = true;
        let listaLinguagens = [];

        while (continuar) {
            let adicionarLinguagem = prompt("Qual tecnologia você gostaria de se especializar?");
            listaLinguagens.push(adicionarLinguagem);

            let sair = prompt("Tem mais alguma tecnologia que você gostaria de aprender? [s/n]");
            if (sair == "n") {
                const imprimir = document.querySelector(".output");

                for (let cont = 0; cont < listaLinguagens.length; cont++) {
                    imprimir.innerHTML += `<p>${listaLinguagens[cont]}</p>`;
                }
                
                continuar = false;                               
            }
        }

    } else if (especial == "Fullstack") {
        alert("A área de Fullstack é muito legal!");

        let continuar = true;
        let listaLinguagens = [];

        while (continuar) {
            let adicionarLinguagem = prompt("Qual tecnologia você gostaria de se especializar?");
            listaLinguagens.push(adicionarLinguagem);

            let sair = prompt("Tem mais alguma tecnologia que você gostaria de aprender? [s/n]");
            if (sair == "n") {
                const imprimir = document.querySelector(".output");

                for (let cont = 0; cont < listaLinguagens.length; cont++) {
                    imprimir.innerHTML += `<p>${listaLinguagens[cont]}</p>`;
                }
                
                continuar = false;                               
            }
        }
    }

} else if (first == "Back-End") {
    const back = prompt("Você quer aprender C# ou Java?");

    const especial = prompt(`Você quer se especializar na área de ${back} ou se desenvolver para Fullstack?`);

    if (especial == back) {
        alert(`A área de ${especial} é muito legal!`);

        let continuar = true;
        let listaLinguagens = [];

        while (continuar) {
            let adicionarLinguagem = prompt("Qual tecnologia você gostaria de se especializar?");
            listaLinguagens.push(adicionarLinguagem);

            let sair = prompt("Tem mais alguma tecnologia que você gostaria de aprender? [s/n]");
            if (sair == "n") {
                const imprimir = document.querySelector(".output");

                for (let cont = 0; cont < listaLinguagens.length; cont++) {
                    imprimir.innerHTML += `<p>${listaLinguagens[cont]}</p>`;
                }
                
                continuar = false;                               
            }
        }
        
    } else if (especial == "Fullstack") {
        alert("A área de Fullstack é muito legal!");

        let continuar = true;
        let listaLinguagens = [];

        while (continuar) {
            let adicionarLinguagem = prompt("Qual tecnologia você gostaria de se especializar?");
            listaLinguagens.push(adicionarLinguagem);

            let sair = prompt("Tem mais alguma tecnologia que você gostaria de aprender? [s/n]");
            if (sair == "n") {
                const imprimir = document.querySelector(".output");

                for (let cont = 0; cont < listaLinguagens.length; cont++) {
                    imprimir.innerHTML += `<p>${listaLinguagens[cont]}</p>`;
                }
                
                continuar = false;                               
            }
        }
    }

} else {
    alert("Resposta inválida!");
}
