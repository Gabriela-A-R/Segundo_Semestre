#%% CLASSES E METODOS:

class Pessoa:
    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.__cpf = cpf #--> os __ = atributo publico

    def get_cpf(self): # esse metodo esta dentro da classe, por tanto ele tem acesso a todos os atributos publicos e privados. ## o metodo get e set só conseguem exibir os atributos privados pois eles são metodos publicos, mas se fossem privados não conseguiriam tbm; mesmo esquema: __ passa o metodo a ser privado; #### get = retorna valor de um atributo
        return self.__cpf
    
    def set_cpf(self, cpf:str): # essse metodo modifica o valor do atributo dentro da classes (atributos publicos e privados)
        #TODO: Incluir um tratamento do valor recebido(AQUI QUE VEM OS TRATAMENTOS DE ERROS TBM) ## todo é uma forma de falar que aqui vem mais uma coisa antes do metodo em si; 
        self.__cpf = cpf

    def exibir_informacoes(self):
        print('Nome:', self.nome)
        print('Idade:', self.__cpf)

#%% PROGRAMA PRINCIPAL:
pessoa1 = Pessoa('Andressa','123.456.789-00')
print(pessoa1.nome)
print(pessoa1.get_cpf())
pessoa1.exibir_informacoes()

#%% aTRIBUTOS ESTATICOS (SEM O SELF):

class Pessoa:
    total_pessoas = 0 #isso aqui é uma variavel que pertence a classe, então quando eu utilizo ela na funçao/metodo contrutor, eu não presciso do self, pois eu não estou definindo nada, estou so "movimentando/manipulando" a variavel.

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf
        Pessoa.total_pessoas += 1

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("CPF:", self.__cpf)

#%% PROGRAMA PRINCIPAL #2
pessoa1 = Pessoa("João", 30, "123.456.789-00")
pessoa1.exibir_informacoes()

pessoa2 = Pessoa("Maria", 25, "987.654.321-00")
pessoa2.exibir_informacoes()

print("Total de pessoas:", Pessoa.total_pessoas) # por a variavel está dentro da classe e "pertencer" a mesma, na hora de "manipula-la" em vez de associa-la a um metodo/função, associamos-la a propria Classe

print("Total de pessoas:", pessoa1.total_pessoas) 
print("Total de pessoas:", pessoa2.total_pessoas)# isso tambem dará certo e retornara o mesmo valor da pessoa1 pois a variavel total_pessoas é uma variavel compartilhada nos metodo construtor, por tanto todos podem acessar
