function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fAno = document.getElementById("txtano")
    var res = document.querySelector("div#res")
    if (fAno.value.length == 0 || fAno.value > ano) {
        window.alert("[ERRO] Verifique os dados e tente novamente!")
    } else {
        var fSex = document.getElementsByName("radsex")
        var idade = ano - Number(fAno.value)
        res.innerHTML = `Idade calculada: ${idade}`
        var genero = ""
        var img = document.createElement("img")
        img.setAttribute("id", "foto")
        if (fSex[0].checked) {
            genero = "Homem"
            if (idade >= 0 && idade < 10) {
                img.setAttribute("src", "bebe_menino.png")
            } else if (idade < 21) {
                img.setAttribute("src", "adolescente_menino.png")
            } else if (idade < 50) {
                img.setAttribute("src", "adulto_homem.png")
            } else {
                img.setAttribute("src", "idoso_homem.png")
            }
        } else if (fSex[1].checked) {
            genero = "Mulher"
            if (idade >= 0 && idade < 10) {
                img.setAttribute("src", "bebe_menina.png")
            } else if (idade < 21) {
                img.setAttribute("src", "adolescente_menina.png")
            } else if (idade < 50) {
                img.setAttribute("src", "adulta_mulher.png")
            } else {
                img.setAttribute("src", "idosa_mulher.png")
            }
        }
        res.style.textAlign = "center"
        res.innerHTML = `Detectamos ${genero} com ${idade} anos.`
        res.appendChild(img)
    }
}
