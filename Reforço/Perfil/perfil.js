async function buscarPokemon(){
    let url = 'https://pokeapi.co/api/v2/pokemon-form/1025/'
    let api = await fetch(url,{
        method: 'GET'
    })

    if(api.ok){
        let resposta = await api.json();
        document.getElementById('txt-nome').innerHTML = resposta.name
        document.getElementById('txt-idade').innerHTML = resposta.id
        document.getElementById('img_perfil').src = resposta.sprites.front_default

        console.log(resposta.sprites)
    }
}

buscarPokemon()