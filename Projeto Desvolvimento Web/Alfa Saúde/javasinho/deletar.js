async function deletarEndereco(id) {
    const token = localStorage.getItem('access_token');
    
    if (!token) {
        alert('Token não encontrado.');
        return;
    }

    const resposta = await fetch('https://go-wash-api.onrender.com/api/auth/address/' + id, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    const result = await resposta.json(); 
    
    if (resposta.ok) {
        alert(result.message || 'Endereço deletado com sucesso.');
        listarEndereco(); 
    } else {
        alert(result.message || 'Erro ao deletar endereço.');
    }
}
