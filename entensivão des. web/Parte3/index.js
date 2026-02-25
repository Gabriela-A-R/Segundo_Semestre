//const minhaPromise = new Promise((resolve, reject) => {
//    let sucesso = true;
//
//    if (sucesso) {
//      resolve("A operação foi bem-sucedida!");
//    } else {
//      reject("A operação falhou.");
//    }
//});


//minhaPromise
//  .then((mensagemSucesso) => {
//    console.log(mensagemSucesso); // Executado se a promise foi resolvida
//    return "Passo adicional após o sucesso";
//  })
//  .then((novaMensagem) => {
//    console.log(novaMensagem); // Continuando o encadeamento após a primeira operação
//  })
//  .catch((mensagemErro) => {
//    console.error(mensagemErro); // Executado se a promise foi rejeitada
//  })
//  .finally(() => {
//    console.log("Operação concluída!"); // Executado sempre, independente do resultado
//  });


const minhaPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
      const sucesso = Math.random() > 0.5; // Define sucesso com 50% de chance
  
      if (sucesso) {
        resolve("Dados recebidos com sucesso!");
      } else {
        reject("Erro ao buscar os dados.");
      }
    }, 2000);
  });
  
  minhaPromise
    .then((mensagemSucesso) => {
      console.log(mensagemSucesso);
      return "Processando os dados..."; // Passa essa mensagem para o próximo .then()
    })
    .then((novaMensagem) => {
      console.log(novaMensagem);
    })
    .catch((mensagemErro) => {
      console.error(mensagemErro);
    })
    .finally(() => {
      console.log("Requisição finalizada!");
    });
  
