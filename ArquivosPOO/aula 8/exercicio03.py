#A associação entre classes ocorre quando uma classe possui atributos que são objetos de outra classe. De acordo com esse conceito, Implemente o
# diagrama de classes abaixo, que representa uma associação onde uma
# Pessoa possui zero ou 1 Carro. Crie um programa principal para testar sua implementação. Utilize o seguinte trecho de código para testar sua implementação

#%%

class Carro:
    def __init__(self, marca:str, modelo:str, placa:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano 

class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
        self.carro = None

    def comprar_carro(self, carro:Carro):
        self.carro = carro

#%%__PROGRAMA PRINCIPAL:


meucarro = Carro('Volkswagem', 'Golf', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome:', eu.nome) # imprime: João
print('Modelo do meu carro:', eu.carro.modelo) # imprime: Golf
print('Placa do meu carro:', eu.carro.placa) # imprime: AAA-1111
# %%
