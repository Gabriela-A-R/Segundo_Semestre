#%% HERANÇA:
class Veiculo: ## Classe mãe, classe que é "principl" classe e as demais herdam dela 

    def __init__(self, marca, modelo, placa): ### nesse caso essa clase só tem o metodo construtor que pode ser usados em outras classes 
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

class Carro(Veiculo): # aqui é a classe filha que tem esse nome por herdar da classe mãe... herda = class tal (da tal):

    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa) # super serve para chamar o metodo da superclasse (classe mãe), se não coolocar ele, o metodo pode se proprio chamar 
        self.portas = portas

    def exibir(self):
        print('---------------------')
        print('Marca: ', self.marca)
        print('Modelo: ', self.modelo)
        print('Placa: ', self.placa)
        print('Portas: ', self.portas)

#%% Programa Principal

carro1 = Carro("Ford", "Ka", "AAA-1234", 4)
carro1.exibir()

##------------------------------------------------------------------------------------------------------------------------------------------------##
#%% sobrescrita de métodos:

class Animal:

    def fazer_som(self): ## definimos um metodo na super classe(classe mãe)
        print("Som genérico de animal")

class Gato(Animal):
    def fazer_som(self): ### gato não tem um som generigo, então em veez de chamar o super.fazer_som, eu sobre escrevo o som especifico...
        print("Miau")

class Cachorro(Animal):
    def fazer_som(self): #### se eu quiser puxar o som generico e add um som eu chamo o super() e add mais um som como "atributo"
        super().fazer_som(self)
        print("Au au")

