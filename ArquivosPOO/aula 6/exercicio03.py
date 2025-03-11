#Implemente a classe Televisao. Atributos: canal (o canal inicial da tv deve ser zero);volume (o volume inicial da tv deve ser zero) _ Métodos: aumentarVolume: aumenta o nível de volume em uma unidade.;diminuirVolume: diminui o nível de volume em uma unidade.;alterarCanal: recebe o número do canal que será sintonizado e altera o canal da tv. B) Faça um programa para criar um objeto da classe Televisao e testar a sua classe.

#%%__CRIA CLASSE;
class Televisao:
    def __init__(self):
        self.canal = 0
        self.volume = 0
    
    def setAumentarVolume(self): #--> metodos
        self.volume += 1

    def setDiminuirVolume(self):
        self.volume -= 1

    def setAlterarCanal(self, canal):
        self.canal = canal

#%%_TESTE:

tv = Televisao()
tv.setAlterarCanal(5)
tv.setAumentarVolume()
tv.setAumentarVolume()
tv.setAumentarVolume()
tv.setDiminuirVolume()
print("A tv está no canal", tv.canal) # A tv está no canal 5
print("A tv está no volume", tv.volume) # A tv está no volume 2