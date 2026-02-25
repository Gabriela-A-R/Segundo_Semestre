function soma(){
    valor1 = parseFloat(document.getElementById('valor1').value);
    valor2 = parseFloat(document.getElementById('valor2').value);

    resultado = valor1+valor2;

    alert('O resultado de '+ valor1+ '+' +valor2 +'='+resultado);
}