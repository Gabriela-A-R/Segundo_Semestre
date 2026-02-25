const url = "https://go-wash-api.onrender.com/api/user";

const token = localStorage.getItem('access_token')

async function cadastro() {
    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let birthday = document.getElementById('birthday').value;
    let password = document.getElementById('password').value;
    let cpf_cnpj = document.getElementById('cpf_cnpj').value.replace(/\D/g, '');

    if (!name) {
        alert('O campo nome é obrigatório.');
        return;
    }

    if (!email) {
        alert('O campo email é obrigatório.');
        return;
    }

    if (!birthday) {
        alert('O campo data de nascimento é obrigatório.');
        return;
    }

    if (password.length < 6) {
        alert('A senha deve conter pelo menos 6 caracteres.');
        return;
    }

    if (!cpf_cnpj) {
        alert('O campo CPF/CNPJ é obrigatório.');
        return;
    }

    if (cpf_cnpj.length < 11 || cpf_cnpj.length > 14) {
        alert('O CPF/CNPJ deve conter entre 11 e 14 números.');
        return;
    }

    let api = await fetch(url, {
        method: "POST",
        body: JSON.stringify({
            'name': name,
            'email': email,
            'user_type_id': 1,
            'password': password,
            'cpf_cnpj': cpf_cnpj,
            'terms': 1,
            'birthday': birthday,
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (api.ok) {
        let resposta = await api.json();
        console.log(resposta);
        alert('Cadastro concluído com sucesso!');
        window.location.href = "login.html";

    } else {
        let respostaError = await api.json();
        console.error(respostaError);

        if (respostaError.data.errors.email) {
            alert("Erro no cadastro: O email já está cadastrado.");
        }
        if (respostaError.data.errors.cpf_cnpj) {
            alert("Erro no cadastro: O CPF já está cadastrado.");
        }
        
    }
}

