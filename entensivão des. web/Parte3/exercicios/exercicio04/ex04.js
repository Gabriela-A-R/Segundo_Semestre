function verificarNumero(numero) {
    numero = parseInt(prompt('Digite um número: '))
    return new Promise((resolve, reject) => {
        if (numero > 10) {
            resolve ('Número válido.')
        } else {
            reject ('Número inválido.')
        }
    })
}

verificarNumero()
    .then((msgSucesso) => {
        console.log(msgSucesso)
    })
    
    .catch((msgErro) => {
        console.error(msgErro)
    })

    .finally(() => {
        console.log('Fim da operação.')
    })