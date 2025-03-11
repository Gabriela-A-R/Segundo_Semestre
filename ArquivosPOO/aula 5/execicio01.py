#Crie um programa em Python que simule o seguinte cenário: durante as Olimpíadas, uma 
# pesquisa foi realizada com 100 pessoas para saber quais esportes olímpicos eles 
# assistiram. Os esportes incluídos na pesquisa foram: judô, vôlei de praia, 
# ginástica e surfe. As respostas foram compiladas, e agora você tem conjuntos de 
# pessoas que assistiram a cada um desses esportes. Calcule a probabilidade de que uma 
# pessoa sorteada aleatoriamente tenha assistido: a)Judô ou surfe; b)Pelo menos dois 
# esportes; c) Todos os esportes; d)Nenhum esporte.
#As pessoas devem ser identificadas pelo seu CPF. Crie um conjunto com 100
# CPFs fictícios distintos para representar todas as pessoas que foram
# entrevistadas e subconjuntos para representar cada esporte. Crie um
# dicionário para armazenar os subconjuntos associados a cada esporte:


#%% IMPORTAÇÕES:
import random

#%%__ função para gerar os CPFs ficticios:

def gerar_cpf():
    return "".join([str(random.randint(0, 9)) for _ in range(9)])

#%%__função para gerar subconjuntos de tamanhos aleatorios:

def gerar_subconjunto(conjunto):
    return set(random.sample(
        list(conjunto), int(random.random() * 100)
        )
    )

#%%__função para calcular a probabilidade:

def calcularPro(subconjunto):
    return len(subconjunto)/100
# %%__programa principal:
pessoas = set() #--> o operador de atribuição: set serve serve para mostrar que pessoas é uma variavel do tipo conjunto conjunto

while len(pessoas)<100:
    pessoas.add(gerar_cpf()) #--> gera os cpfs

esportes = {
    'surf':gerar_subconjunto(pessoas),
    'volei':gerar_subconjunto(pessoas),
    'ginastica':gerar_subconjunto(pessoas),
    'judo':gerar_subconjunto(pessoas)
}

print(esportes)

