//ex1

//Promise
const simulacao = new Promise((resolve, reject) => {
    const sucesso = Math.random() > 0.5 //50% de chance

    setTimeout(() => {
        if (sucesso) {
            resolve('Operação bem-sucedida.')
        } else {
            reject('Operação falhou.')
        }
    }, 1000) //timer de 1 sec
})

//codigo principal
simulacao
    .then((mensagemSucesso) => {
        console.log(mensagemSucesso)
    })
    .catch((mensagemErro) => {
        console.log(mensagemErro)
    })
    .finally(() => {
        console.log('Processo finalizado')
    })
