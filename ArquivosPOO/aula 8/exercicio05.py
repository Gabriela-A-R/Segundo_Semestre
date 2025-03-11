# Observe o diagrama de classes abaixo e implemente as classes Carro e Pneu. Classe Pneu_Atributos: pressao (valor inteiro que indica a pressão de ar no pneu.) Métodos: furar(simula pneu furado, alterando o valor do atributo pressao para zero). Classe Carro_Atributos: ligado (valor booleano que indica se o carro está ligado ou desligado. Definido no construtor com o valor False); pneu1, pneu2, pneu3, pneu4 (objetos do tipo Pneu). Métodos: ligar (altera o valor do atributo ligado para True); desligar(altera o valor do atributo ligado para False); verificar_pneu(se o carro estiver ligado, esse método deve exibir a pressão em cada um dos pneus. Se o carro estiver desligado, o método deve exibir a mensagem ‘Carro Desligado’). Utilize o trecho de código abaixo como programa principal para testar sua implementação

#%%__CLASSES E METODOS:
class Pneu:
    def __init__(self, pressao:int):
        self.pressao = pressao

    def furar(self):
        self.pressao = 0

class Carro:
    def __init__(self, pneu1:Pneu, pneu2:Pneu, pneu3:Pneu, pneu4:Pneu):
        self.pneu1 = pneu1
        self.pneu2 = pneu2
        self.pneu3 = pneu3
        self.pneu4 = pneu4
        self.ligado = False
    
    def ligar(self):
        if self.ligado == False:
            self.ligado = True
    
    def desligar(self):
        if self.ligado == True:
            self.ligado = False

    def verificar_pneu(self):
        if self.ligado == True:
            print(f'Pressão do pneu 1: {self.pneu1.pressao}, presão do pneu 2: {self.pneu2.pressao}, pressão do pneu 3: {self.pneu3.pressao} e pressão do pneu 4: {self.pneu4.pressao}')
        else:
            print('Carro Desligado')

#%%__PROGRAMA PRINCIPAL:

p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro (p1, p2, p3, p4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu() # exibir a pressão em cada pneu
meucarro.desligar()
meucarro.verificar_pneu() # exibir carro está desligado.