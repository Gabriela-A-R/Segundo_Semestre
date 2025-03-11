#%% __CLASSES E METODOS:

class Endereco:
    def __init__(self, rua, endereco, bairro, complemento, cep):
        self.rua = rua
        self.endereco = endereco
        self.bairro = bairro
        self.complemento = complemento
        self.cep = cep

    def exibir_dados1(self):
        print('Dados do endereço: ')
        print(' rua:', self.rua)
        print(' endereco:', self.endereco)
        print(' bairro:', self.bairro)
        print(' complemento:', self.complemento)
        print(' cep:', self.cep)

class Funcionario:

    def __init__(self, nome:str, data_nasc:str, sexo:str, salario:float,
endereco:Endereco):
        self.nome = nome
        self.data_nasc = data_nasc
        self.sexo = sexo
        self.salario = salario
        self.endereco = endereco # objeto da classe Endereco

    def exibir_dados(self):
        print('Dados do funcionário:')
        print('nome: ', self.nome)
        print('data_nasc:', self.data_nasc)
        print('sexo:', self.sexo)
        print('salario:', self.salario)
        self.endereco.exibir_dados1()

#%%__PROGRAMA PRINCIPAL:

endereco1 = Endereco('rua dos bobos', '0', 'dos bocos', '--', '00000-000')
print(endereco1.rua)
endereco1.exibir_dados1()

funcionario1 = Funcionario('daniela', '01/01/1901', 'feminino', 1200,00,)
funcionario1.exibir_dados() ### isso não esta rodando...
