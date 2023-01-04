function fatorial(n) {
    let fat = 1
    for (let c = n; c > 1; c--) {
        fat *= c
    }
    return fat
}

// Fatorial de forma recursiva:
function fatorialRecursivo(n) {
    if (n == 1) {
        return 1
    } else {
        return n * fatorial(n-1)
    }
}

function parImpar(n) {
    if (n % 2 == 0) {
        return "PAR"
    } else {
        return "ÍMPAR"
    }
}

function soma(n1, n2=0) {
    return n1 + n2
}

let v = function(x, y=1) {
    return x * y
}

console.log(fatorial(5))
console.log(fatorialRecursivo(5))
console.log(parImpar(5))
console.log(soma(5, 10))
console.log(v(5))
