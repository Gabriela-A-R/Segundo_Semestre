fetch('https://api.publicapis.org/entries') // URL do recurso
  .then(response => response.json()) // converte a resposta em JSON
  .then(data => console.log(data))   // manipula os dados recebidos
  .catch(error => console.error('Erro:', error)); // trata erros

////////

fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title: 'Novo Post',
    body: 'Este é o conteúdo do post.',
    userId: 1
  })
})
  .then(response => response.json()) // converte a resposta para JSON
  .then(data => console.log(data))   // exibe os dados recebidos
  .catch(error => console.error('Erro:', error)); // trata erros

//////////
fetch('https://api.publicapis.org/entries')
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro na requisição');
        }
        return response.json(); // converte para JSON
    })
    .then(data => console.log(data)) // exibe os dados no console
    .catch(error => console.error('Erro:', error));
