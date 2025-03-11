#%%____TRATAMENTO DE EXCEÇOES:
try:
    # código suscetível a falha
    # o try vai ser usado para tentar usar o bloco de codigo que vem aqui e se existir alguma exeção, ele não interrompe o codigo ele vai tratar, com:except
    pass

except:
    # código executado após ocorrer um erro
    ## aqui fica o bloco de codigo que será execultado quando o de cima der algum erro. o proprio tratamento de erros. Oexcept só vai acontecer se tiver uma exesação
    ## posso ter em um programa quantos except eu achar nescessario
    pass

else:
    # código executado apenas se nenhum erro ocorrer
    ### agora se não... eu execulto o que tiver aqui (o else é opicional)
    pass

finally:
    # código executado sempre, se deu certo ou não 
    pass

#%%___EXEMPLO:

class Paciente:
    def __init__(self, nome:str):
        if not isinstance(nome,str):
            raise TypeError("'nome' inválido")
        if nome == '':
            raise NameIsEmptyError("'nome' é obrigatório")
        self.nome = nome
class NameIsEmptyError(Exception):
    pass

try:
    nome = input('Digite o nome do paciente: ')
    p = Paciente(nome)

except TypeError:
    print('O nome deve ser uma string') ## isso tá errado, ou melhor por conta do input estar como str numeros tbm se trasformam em letras. 

except NameIsEmptyError:
    print('O nome não pode ser uma string vazia')

except Exception as e:
    print('Ocorreu um erro inesperado ao criar o objeto')
    print('informações do erro:', e)


# %%
