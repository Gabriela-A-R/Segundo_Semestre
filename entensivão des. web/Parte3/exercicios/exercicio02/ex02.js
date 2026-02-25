//promise
const tempo = new Promise((resolve) => {
    setTimeout(() => {
            resolve ('Tempo finalizado!')
    }, 2000)
})

//principal
tempo
    .then((msgSucesso) => {
        console.log(msgSucesso)
    })
    .finally(() => {
        console.log('Contagem completa.')
    })