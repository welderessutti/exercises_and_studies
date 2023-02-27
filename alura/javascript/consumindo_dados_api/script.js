/* // Usando then, catch, finally:
var consultaCep = fetch("https://viacep.com.br/ws/13333070/json/")
.then(resposta => resposta.json())
.then(r => {
    if (r.erro) {
        throw Error("Esse CEP não existe!")
    } else {
    console.log(r)
}})
.catch(erro => console.log(erro))
.finally(mensagem => console.log("Processamento concluído!"));

console.log(consultaCep);
*/

// Usando async e await:
async function buscaEndereco(cep) {

    var mensagemErro = document.getElementById("erro")
    mensagemErro.innerHTML = "";

    try {
        var consultaCep = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        var consultaCepCovertida = await consultaCep.json();

        if (consultaCepCovertida.erro) {
            throw Error("CEP não existente!");
        }

        var cidade = document.getElementById("cidade");
        var logradouro = document.getElementById("endereco");
        var estado = document.getElementById("estado");
        var bairro = document.getElementById("bairro");

        cidade.value = consultaCepCovertida.localidade;
        logradouro.value = consultaCepCovertida.logradouro;
        estado.value = consultaCepCovertida.uf;
        bairro.value = consultaCepCovertida.bairro;

        console.log(consultaCepCovertida);

        return consultaCepCovertida;

    } catch (erro) {
        mensagemErro.innerHTML = `<p>CEP inválido. Tente novamente!</p>`
        console.log(erro);
    }
}

/* // Promise.all ajudar a executar varias promises:
let ceps = ["05501000", "13355070"];
let conjutoCeps = ceps.map(valores => buscaEndereco(valores));
console.log(conjutoCeps);
Promise.all(conjutoCeps).then(respostas => console.log(respostas));
*/

var cep = document.getElementById("cep");
cep.addEventListener("focusout", () => buscaEndereco(cep.value));
