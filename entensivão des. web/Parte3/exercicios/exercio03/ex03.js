const Operacao = new Promise((resolve, reject) => {
    setTimeout(() => {
        const numero = Math.random()
        
        if (numero > 0.7) {
            resolve ('Operação completa!')
        } else {
            reject ('Erro na operação!')
        }
    }, 1000)
})

Operacao
    .then((msgSucesso) => {
        console.log (msgSucesso)
    })

    .catch((msgErro) => {
        console.error(msgErro)
    })

    .finally(() => {
        console.log('Fim da operação.')
    })