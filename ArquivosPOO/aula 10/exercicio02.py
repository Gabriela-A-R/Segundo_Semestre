#Implemente a classe Filme, conforme o diagrama de classes abaixo Todos
# os atributos devem ser privados Crie os métodos getters e setters para
# todos os atributos
# No seu programa principal, faça a seguinte implementação:
#- Cadastrar 3 filmes (com os dados informados pelo usuário)
#- Armazenar os dados de cada filme em um objeto da classe Filme
#- Armazenar os objetos em um vetor
#- Exibir um relatório com os dados de todos os filmes cadastrados.
#%%CLASE:
class Filme:
    def __init__(self, titulo:str, genero:str):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo
    def get_genero(self):
        return self.__genero
    
    def set_titulo(self, titulo:str):
        self.__titulo = titulo
    def set_genero(self, genero:str):
        self.__genero = genero

#%%
