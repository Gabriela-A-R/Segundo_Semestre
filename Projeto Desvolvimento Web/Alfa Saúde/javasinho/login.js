const url = 'https://go-wash-api.onrender.com/api/login';

async function login(event) {
    event.preventDefault(); 

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!email) {
        alert('O campo email é obrigatório.');
        return;
    }

    if (!password) {
        alert('O campo senha é obrigatório.');
        return;
    }

    const data = {
        email: email,
        password: password,
        user_type_id: 1
    };

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), 
    });

    const result = await response.json();

    if (response.ok) {
        localStorage.setItem('access_token', result.access_token);
        alert(result.message || 'Login realizado com sucesso!');
        window.location.href = "home.html";
    } else {
        alert(result.message || 'Erro ao realizar o login.');
    }
}
document.getElementById('login-formato').addEventListener('submit', login);
