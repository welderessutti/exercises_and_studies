let num = [5, 8, 2, 9, 3]

num.push(100)  // Acrescenta no final da lista.
num.sort()  // Ordena a lista em ordem crescente.

console.log(num)
console.log(`O vetor tem ${num.length} posições.`)
console.log(`O primeiro número do vetor é o ${num[0]}.`)

console.log()

for (let pos = 0; pos < num.length; pos++) {
    console.log(`A posição ${pos} tem o valor ${num[pos]}.`)
}

console.log()

for (let pos in num) {
    console.log(`A posição ${pos} tem o valor ${num[pos]}.`)
}

console.log()

console.log(num.indexOf(555))  // Retorna o índice/posição do elemento. Caso não exista, retorna -1.
 