# Modifique a classe Funcionario para que todos os atibutos se tornem
# privados e crie os métodos getters e setters para todos os atributos.
# Utilize o trecho de programa principal abaixo para testar a implementação da classe.

#%% CLASSES
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    def get_cargo(self):
        return self.__cargo
    def get_salario(self):
        return self.__salario
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_cargo(self, cargo):
        self.__cargo = cargo
    def set_salario(self, salario):
        self.__salario = salario

#%% PROGRAMA PRINCIPAL:

funcionario1 = Funcionario("João", "Desenvolvedor", 5000)
print("Nome:", funcionario1.get_nome())
print("Cargo:", funcionario1.get_cargo())
print("Salário:", funcionario1.get_salario())
funcionario1.set_cargo('Analista de sistemas')
print("Cargo:", funcionario1.get_cargo())

funcionario2 = Funcionario("Maria", "Gerente de Projetos", 7000)
print("Nome:", funcionario2.get_nome())
print("Cargo:", funcionario2.get_cargo())
print("Salário:", funcionario2.get_salario())