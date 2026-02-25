async function listarVeiculo() {
    const token = localStorage.getItem('access_token');
    const api = await fetch ('https://go-wash-api.onrender.com/api/auth/vehicle', {
        method:"GET",
        header: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });
    let resposta = await api.json();
    let tabela_veiculo = document.getElementById('tabela_veiculo');
    let row = "";

    resposta.data.forEach(lista_endereco => {
        console.log(lista_endereco);
        row += `<tr>
                    <td>${lista_endereco.id}</td>
                    <td>${lista_endereco.title}</td>
                    <td>${lista_endereco.cep}</td>
                    <td>${lista_endereco.address}</td>
                    <td>${lista_endereco.number}</td>
                    <td>${lista_endereco.complement}</td>
                    <td><input type='button' value='Atualizar' onclick='update(${lista_endereco.id})'/>

                    <input type='button' value='Deletar'
                    onclick = 'deletarEndereco(${lista_endereco.id})'/></td>
                </tr>`
    });
    tabela_veiculo.innerHTML = row;
}

listarVeiculo();

function update(id) {
    window.location.href = `atualizar.html?id=${id}`;
}

