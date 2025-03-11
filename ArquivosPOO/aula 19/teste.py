f = open('teste.txt', 'w') ## abro o arquivo de texto
f.write('Ola Mundo!\n') ## insiro o que quero
f.close() ## fecho o arquivo 

with open('teste.txt', 'w')  as f: ##permite abrir o arquivo, executar o que é necessário e garante que o arquivo será fechado ao final das instruções
    f.write('Olá novamente!\n')

with open('teste.txt', 'r') as f: #read e readlines: lê todo o conteúdo, retornando str ou list[str]
    texto = f.read()

with open('teste.txt', 'r') as f: #readline: lê o conteúdo do arquivo a partir da posição do marcador até encontrar uma quebra de linha
    texto = f.readline()

with open('teste.txt', 'r') as f: #tell e seek: Lê e modifica a posição do marcador
    print(f.tell()) # exibe a posição atual
    f.seek(5) # move a posição atual para o índice 5

texto = 'escrevendo a primeira frase'
with open('teste.txt', 'w') as f: #write e writelines: escreve o conteúdo de uma str ou sequência de str no arquivo
    f.write(texto)

#%%
import pandas as pd

df = pd.read_csv('pets.csv') # serve para fazer a leitura do arquivo
print(df) # printa tudinho
print('-----------')
print(df['nome']) # printa so a coluna especifica
print('-----------')
print(df['nome'][2]) # printa a linha da coluna especifica 

df.to_csv('bichinhos.csv') # cria uma copia num arquivo novo

# %%
import json

dados = {"nome": "Alice", "idade": 30} #cria uma tabela

with open('dados.json', 'w') as arquivo: # abre/cria um arquivo JSON e add a tabela
    json.dump(dados, arquivo)
    
with open('dados.json', 'r') as arquivo: # abre o arquivo, e mostra o arquivo.
    dados_arquivo = json.load(arquivo)
print(dados_arquivo)

with open('dados.json', 'r') as arquivo:
    dados_arquivo = json.load(arquivo)
    dados_arquivo['nome'] = 'vitor' # modifica o valor da variavel se tiver a coluna. se não tiver ele add (usa o mesmo raciocinio do dicionario)
    json.dump(dados_arquivo, arquivo)
    

    # %%
