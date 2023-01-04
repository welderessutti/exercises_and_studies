function getRandomInt(min, max, numbersToExclude) {

    min = Math.ceil(min);
    max = Math.floor(max);
    const random = Math.floor(Math.random() * (max - min) + min)
    return numbersToExclude.includes(random)? getRandomInt(min, max, numbers): random;
}

function megasena(qt, numbers=[]) {
    numbers.push(getRandomInt(1, 61, numbers))
    return qt-1>0? megasena(qt-1, numbers): numbers
}

console.log(megasena(6))
