#%%__FORMA PARA CRIAR CLASSES:

class Professor:
    def __init__(self): #--> init é o metodo contrustor (serve para formatar/criar um objeto)
        self.nome = "Vitor"
        self.matricula = '12345'
        self.contratacao = '01/01/2024'
        self.disciplina = 'POO' #--> valor fixo

class Professor:
    def __init__(self, nome, matri, contrata, disc):
        self.nome = nome
        self.matricula = matri
        self.contratacao = contrata 
        self.disciplina = disc #--> aqui eu passei os parametros (junto com o self), e por isso consigo "usar" a mesma forma pra diversos objetos(no caso professor)
    
    def setDisciplina(self, disc): #--> definir os metodos setALGUMACOISA
        self.disciplina = disc


#%%__CRIANDO INSTANCIAS:

prof1 = Professor("vitor", 12345, '01/01/2025', 'POO') #--> cria a intancia com seus atributos
print(prof1.nome) #--> mostra somente o nome 

prof1.setDisciplina('FDB') #--> modifico a disciplina, o valor do atributo no caso

