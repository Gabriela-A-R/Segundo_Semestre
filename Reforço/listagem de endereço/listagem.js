listarEndereco()
async function listarEndereco(){
    // integração
    api = await fetch('https://go-wash-api.onrender.com/api/auth/address', {
        method:"GET",
        headers: {
            'Authorization' : 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOi8vYXBpLWdvLXdhc23Lmhlcm9rdWFwcC5jb20vYXBpL2xvZ2luIiwiaWF0IjoxNzEwNDE3MjIyLCJuYmYiOjE3MTA0MTcyMjIsImp0aSI6InBsZll0aENEZ0U1NUNzMHEiLCJzdWIiOiIxIiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.z1pdEBkx8Hq01B7jNKa42NGxtFFHwb-7O_0y8krVWUY'
        }
    })
    /*resposta = await api.json()
    for(let i = 0; i<resposta.data.length; i++){
        console.log(resposta.data[i])
    }*/
    //ou

    resposta = await api.json()
    resposta.data.forEach(endereco => {
        console.log(endereco)
    })
   //array= [{},{}];
   //array.forEach

}
listarEndereco()
