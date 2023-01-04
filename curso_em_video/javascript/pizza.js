function temFatia(n) {
    if (n > 0) {
        return true
    } else {
        return false
    }
}

function comeFatia(n) {
    n -= 1
    return n
}

function comerPizza(n) {
    while (temFatia(n)) {
        n = comeFatia(n)
    }
    return n
}

pizza = 8
pizza = comerPizza(pizza)

console.log(pizza)
