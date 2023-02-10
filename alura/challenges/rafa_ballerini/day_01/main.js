const numeroUm = 1
const stringUm = "1"
const numeroTrinta = 30
const stringTrinta = "30"
const numeroDez = 10
const stringDez = "10"

if (numeroUm === stringUm) {
    console.log(`As variáveis numeroUm (${typeof(numeroUm)}) e stringUm (${typeof(stringUm)}) tem o mesmo valor, mas tipos diferentes.`)
} else {
    console.log(`As variáveis numeroUm (${typeof(numeroUm)}) e stringUm (${typeof(stringUm)}) não tem o mesmo valor.`)
}

if (numeroTrinta === stringTrinta) {
    console.log(`As variáveis numeroTrinta (${typeof(numeroTrinta)}) e stringTrinta (${typeof(stringTrinta)}) tem o mesmo valor, mas tipos diferentes.`)
} else {
    console.log(`As variáveis numeroTrinta (${typeof(numeroTrinta)}) e stringTrinta (${typeof(stringTrinta)}) não tem o mesmo valor.`)
}

if (numeroDez === stringDez) {
    console.log(`As variáveis numeroDez (${typeof(numeroDez)}) e stringDez (${typeof(stringDez)}) tem o mesmo valor, mas tipos diferentes.`)
} else {
    console.log(`As variáveis numeroDez (${typeof(numeroDez)}) e stringDez (${typeof(stringDez)}) não tem o mesmo valor.`)
}

console.log(numeroUm == stringUm)
console.log(numeroTrinta == stringTrinta)
console.log(numeroDez == stringDez)
console.log(numeroUm === stringUm)
console.log(numeroTrinta === stringTrinta)
console.log(numeroDez === stringDez)
