const url = new URLSearchParams(location.search)
let id = url.get('id')
const token = localStorage.getItem('access_token')


async function mostrardados(){
    const resposta = await fetch ("https://go-wash-api.onrender.com/api/auth/address/" + id
,{
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    
    if (resposta.ok) {
        const endereco = await resposta.json();
        console.log(endereco);

        document.getElementById("cep").value = endereco.data.cep;
        document.getElementById("titulo").value = endereco.data.title;
        document.getElementById("endereco").value = endereco.data.address;
        document.getElementById("numero").value = endereco.data.number;
        document.getElementById("complemento").value = endereco.data.complement;
    } else {
        console.error("Erro ao carregar o endereço. Código de status:", resposta.status);
        alert("Não foi possível carregar os dados do endereço.");
    }

}
mostrardados()

async function atualizar(){

    let titulo = document.getElementById('titulo').value; 
    let cep = document.getElementById('cep').value;
    let endereco = document.getElementById('endereco').value; 
    let numero = document.getElementById('numero').value;
    let complemento = document.getElementById('complemento').value;

   
    let api = await fetch ("https://go-wash-api.onrender.com/api/auth/address/" + id
,{
        method: "POST",
        headers:{
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}` 
        },
        body: JSON.stringify({
            'title': titulo,
            'cep': cep,
            'address': endereco,
            'number': numero,
            'complement': complemento
        }),
    })

   if(api.ok){
    alert("Cadastro atualizado com êxito!")
    window.location.href = "lista_endereco.html";

   }else{
    console.error("Erro ao atualizar o endereço. Código de status:", resposta.status);
        alert("Não foi possível atualizar o endereço.");
   }
}
atualizar()