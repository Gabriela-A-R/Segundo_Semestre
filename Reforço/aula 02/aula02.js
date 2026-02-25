var dados =[];

function formulario(){
    nome = document.getElementById("nome").value
    cpf = document.getElementById('cpf').value
    data_nascimento = document.getElementById('dtnas').value
    termo = document.getElementById('termo').checked
    idade = document.getElementById('idade').value

    if (idade < 18){
        alert("a idade tem que ser maior que 18")
        return
    }

    if(termo){
        dados.push(nome)
        alert("Cadastro com sucesso")
        listaUsuario()
    } else{
        alert("prescisa aceitar o termo")
    }
}
function listaUsuario(){
    console.log(dados)
}
