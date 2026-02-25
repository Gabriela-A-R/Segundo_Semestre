const url = 'https://go-wash-api.onrender.com/api/auth/address';

const token = localStorage.getItem('access_token')

async function cadastroEndereco(event) {
    event.preventDefault();

    let titulo = document.getElementById('titulo').value; 
    let cep = document.getElementById('cep').value;
    let endereco = document.getElementById('endereco').value; 
    let numero = document.getElementById('numero').value;
    let complemento = document.getElementById('complemento').value;

    
    if (!titulo) {
        alert('O campo título é obrigatório.');
        return;
    }

    if (!cep) {
        alert('O campo CEP é obrigatório.');
        return;
    }

    if (!endereco) {
        alert('O campo endereço é obrigatório.');
        return;
    }

    if (!numero) {
        alert('O campo número é obrigatório.');
        return;
    }

 
    let api = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
            'title': titulo,
            'cep': cep,
            'address': endereco,
            'number': numero,
            'complement': complemento
        }),
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    if (api.ok) {
        let resposta = await api.json()
        alert(resposta.message || 'Cadastro de endereço concluído com sucesso!');
        window.location.href = "home.html";
    } else {
        let respostaError = await api.json();
        alert(respostaError.message || 'Erro no cadastro do endereço.');
    }
}
document.getElementById('form-endereco').addEventListener('submit', cadastroEndereco);