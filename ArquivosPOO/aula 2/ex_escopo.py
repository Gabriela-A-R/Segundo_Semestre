def imprime_x():
    x = 5
    print(f"x no escopo da função: {x}")

x = 10
imprime_x()
print(f"x no escopo global: {x}")

#-------------------------------------------------------------------------
def exemplo_escopo():
    y = 5
    print(f"y = {y}")

exemplo_escopo()
x = 10

print(f"x = {x}")
#print(f"y = {y}") # dá erro pq o y ta dentro do escopo local 

#-------------------------------------------------------------------------
def exemplo_escopo():
    y = 5
    print(f"x = {x}")
    print(f"y = {y}")

x = 10
exemplo_escopo()

#-------------------------------------------------------------------------
def somar(n1,n2):
    soma = n1+n2
    print(soma)

somar(5,6)
somar(3,4)
somar(11,22)

#-------------------------------------------------------------------------
def somar(n1,n2):
    soma = n1+n2
    return soma

x = somar(5,6)
print(f'O valor é {x/2}')
