function calcIdade() {
    let atual = new Date().getFullYear()
    idade.innerHTML = Number(atual) - Number(iano.value)
}
