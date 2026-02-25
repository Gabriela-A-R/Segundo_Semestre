async function name() {
    let url = //http da api
    let api = await fetch(url, {
        method: 'GET'
    })

    if(api.ok){
        let resposta = await api.json();
        document.getElementById().innerHTML = resposta.//variavel
    }

    
}