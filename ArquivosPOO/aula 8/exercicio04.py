#Implemente o diagrama de classes abaixo, que representa uma associação onde um Pedido possui uma lista de 5 Produtos. Crie um programa principal para testar sua implementação. Utilize o trecho de código abaixo como programa principal para testar sua implementação

#%%__CLASSES E METODOS:
class Produto:
    def __init__(self, nome:str, preco:float, qtd:int):
        self.nome = nome
        self.preco = preco
        self.quantidade = qtd

class Pedido:
    def __init__(self):
        self.produtos = [] #--> inicia com uma lista vazia 

    def adicionar_produto(self, produto:Produto):
        self.produtos.append(produto)

    def calcular_valor(self):
        total = 0
        for produto in self.produtos:
            total += produto.quantidade * produto.preco
        return total


    
#%%___PROGRAMA PRINCIPAL:

cafe = Produto('Café solúvel', 5.50, 1)
arroz = Produto('Arroz integral', 4.90, 2)
feijao = Produto('Feijão preto', 2.80, 2)
chocolate = Produto('Ouro Branco', 5.00, 1)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
meu_pedido.adicionar_produto(chocolate)
print('O valor total é:', meu_pedido.calcular_valor())