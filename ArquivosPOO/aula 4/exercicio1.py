#Elabore um programa que crie um dicionário de produtos, inicialmente vazio. Preencha o dicionário com as informações de 5 produtos. 
# Utilize o nome do produto como chave e o preço como valor.
#Solicite os dados ao usuário. Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50,00.

#%%
produtos = {}
# %% __add produtos 

for item in range(5):
    nome_produto = input('Digite o produto:')
    valor_produto = float(input('Valor do produto:'))
    produtos[nome_produto] = valor_produto
    item += 1

# produtos = ['chocolate'] = 10,50
# produtos = ['bala de goma'] = 7,50
# produtos = ['camisa'] = 50,00
# produtos = ['tênis'] = 150,00
# produtos = ['livro'] = 20,00

#%% __ percorrendo o dicionario

for nome, valor in produtos.items():
    if valor >= 50:
        print(f'{nome}: R$ {valor}')