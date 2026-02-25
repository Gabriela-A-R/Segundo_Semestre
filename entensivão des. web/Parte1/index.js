let idade = 18;
let mensagem = (idade >= 18) ? "Maior de idade" : "Menor de idade";
console.log(mensagem); // "Maior de idade"

let frutas = ["Maçã", "Banana", "Laranja"];
    console.log(frutas[1]); // "Maçã"

let temperatura = 30;
if (temperatura > 35) 
    {
    console.log("Muito quente");} 
else if (temperatura > 25) {
    console.log("Quente");}
else {
    console.log("Agradável");}

let diaSemana = 0;

switch (diaSemana) {
    case 1:
        console.log("Segunda-feira");
        break;
    case 2:
        console.log("Terça-feira");
        break;
    case 3:
        console.log("Quarta-feira");
        break;
    default:
        console.log("Dia inválido");
    }