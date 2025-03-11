#Elabore um fluxograma e o respectivo programa em Python que solicita três notas de um aluno em
#uma dada disciplina, calcula a média das notas e exibe a sua situação segundo a tabela: -> maior ou igual a 6; APROVADO -> entre 3 e 6; EXAME -> menor que 3; REPROVADO. 
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))

media = (n1 + n2 + n3)/3

if media >= 6:
    print('APROVADO')
elif media < 3:
    print('REPROVADO')
else:
    print('EXAME')
    