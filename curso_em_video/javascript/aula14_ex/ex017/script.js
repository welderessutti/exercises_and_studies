function tabuada() {
    let num = document.getElementById("txtn")
    let tab = document.getElementById("seltab")

    if (num.value.length == 0) {
        window.alert("Por favor, digite um número!")
    } else {
        let numTab = Number(num.value)
        tab.innerHTML = ""
        for (let c = 1; c <= 10; c++) {
            let item = document.createElement("option")
            item.text = `${numTab} x ${c} = ${numTab * c}`
            item.value = `tab${c}`
            tab.appendChild(item)
        }
    }
}
