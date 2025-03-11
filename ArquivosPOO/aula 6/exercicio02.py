#Crie uma classe que representa um triângulo. Atributos: ladoA;ladoB;ladoC _ Métodos: calcularPerimetro: retorna o perímetro do triângulo (soma dos três lados). B) Crie um programa que utilize esta classe. O programa deve pedir ao usuário que informe as medidas dos três lados de um triângulo. Depois deve criar um objeto com essas medidas e exibir seu perímetro.

#%% __ CRIAR CLASE:
class Triangulo:
    def __init__(self, A:int, B:int, C:int):
        self.ladoA = A
        self.ladoB = B
        self.ladoC = C
    
    def CalcularPerimetro(self) ->int: #--> serve para indicar que retorna um numero inteiro
        return self.ladoA + self.ladoB + self.ladoC

#%%__programa principal:
ladoA = int(input('digite o primeiro lado:'))
ladoB = int(input('digite o segundo lado:'))
ladoC = int(input('digite o terceiro lado:'))

triangulo1 = Triangulo(ladoA, ladoB, ladoC)
print(triangulo1.CalcularPerimetro()) # deu certo, faltava o ()