let pessoa = { nome: "João", idade: 25, nome2: 'Victor', idade2: 18 };

for (let chave in pessoa) {
  console.log(chave, pessoa[chave]); // Exibe "nome João" e "idade 25"
}

//let frutas = ["Maçã", "Banana", "Laranja"];

//for (let i in frutas) {
  //console.log(i, frutas[i]); // Exibe 0 "Maçã", 1 "Banana", 2 "Laranja"
//}

let frutas = ["Maçã", "Banana", "Laranja"];

for (let fruta of frutas) {
  console.log(fruta); // Exibe "Maçã", "Banana", "Laranja"
}


//////////////
//let frutas = ["Maçã", "Banana", "Laranja"];

//frutas.forEach(function(fruta, indice) {
 // console.log(indice, fruta); // Exibe 0 "Maçã", 1 "Banana", 2 "Laranja"
//});


frutas.forEach((fruta, indice) => {
    console.log(indice, fruta); // Exibe 0 "Maçã", 1 "Banana", 2 "Laranja"
  });
////////////////
