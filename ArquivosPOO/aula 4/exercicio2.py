#Escreva uma função que conta a quantidade de vogais em um texto e
# armazena tal quantidade em um dicionário, onde a chave é a vogal
# considerada e o valor é a quantidade de vezes que essa vogal aparece no texto.
# A função deve receber o texto como entrada e retornar o dicionário. 
# Por exemplo, para o texto abaixo: texto = 'faculdade impacta de tecnologia'
#A função deve devolver o seguinte dicionário: {'a': 5, 'u': 1, 'e': 3, 'o' : 2, 'i': 2 }

#%%__função:
def contarVogais(texto):

    vogais = 'aieou'
    contagem = {vogal:0 for vogal in vogais} #-->cria e add coisas no dicionario diante de uma variavel (INCRIVEL); vogal: 0 cria uma chave para cada vogal (como 'a', 'e', 'i', etc.), e o valor inicial de cada chave é 0. Ou seja, estamos dizendo: "Para cada vogal, a contagem inicial é 0". cada vogal é uma chave e o valor associado a ela é 0.

    for letra in texto:
        if letra in vogais:
            contagem[letra] += 1
    return contagem

#%%__main
   
texto = 'faculdade impacta de tecnologia'
resultado = contarVogais(texto)
print(resultado)

# %%
