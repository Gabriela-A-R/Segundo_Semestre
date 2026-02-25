const resultados = new Promise((resolve, reject) => {
    setTimeout(() => {
        const falha = Math.random() > 0.3

        if (falha) {
            reject('Erro no processamento de dados.')
        } else {
            resolve ('Dados processados.')
        }
    }, 3000)
})

resultados
    .then((msgSucesso) => {
        console.log (msgSucesso)
    })
    .catch((msgErro) => {
        console.error (msgErro)
    })
    .finally(() => {
        console.log ('Processo finalizado')
    })