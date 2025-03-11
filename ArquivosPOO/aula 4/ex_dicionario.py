#%%
contatos = {}

#%% ___add ao dicionario 
contatos ["Pedro"] = '123456789'
contatos ["Maria"] = '101112131'
contatos ["Teresa"] = '141516171'

contatos [123] = 'laranja' 
contatos ["Roberto"] = 123455789
#--> dicionario pode ser hetorogenio, podem ser inteiros com string ou vice-verça

#%% __serve para remover esse item 
contatos.pop('Pedro') #--> 

#%% __para percorrer o dicionario:

for item in contatos:
    print(item) #imprime apenas a chave do dicionario

for item in contatos:
    print(contatos[item]) #imprime a apenas a chave dos itens do dicionario

for chave, valor in contatos.items():
    print(chave)
    print(valor)
    print('=-=-=-=\n') # imprime a chave e o seu respectivo valor

# %% __verificando item
valor_procurado = '123456789'
for chave, valor in contatos.items():
    if valor == valor_procurado:
        print(f'Valor encontrado em {chave}')
   
# %%
