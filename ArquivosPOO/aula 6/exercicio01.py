#Implemente a classe Livro, conforme o diagrama a seguir. No programa principal, crie dois objetos da classe Livro. Atributos: Título; Autor; QuantidadePaginas _ Métodos: Essa classe não possui métodos

#%%__CRIANDO A CLASSE:
class Livro:
    def __init__(self, titulo:str, autor:str, quatpag:int):
        self.Titulo = titulo
        self.Autor = autor
        self.QuantidadePaginas = quatpag
        
# %%
livro1 = Livro('Uma Rosa no Concreto', 'Angie Thomas', 308)
livro2 = Livro('Grampo Federal', 'Eduardo', 144)

print(f'Os livros: {livro1.Titulo} e {livro2.Titulo} estão adicionados com sucesso')

titulo = input('Digite o Titulo:')
autor = input("Digite o nome do autor:")
paginas = int(input('Quantas paginas:'))

livro3 = Livro(titulo, autor, paginas)
print(livro3.Titulo)
print(livro3.Autor)