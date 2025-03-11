#%% # separa por etapas
nubank = set(['ana', 'bia', 'clara', 'duda', 'fabio'])
c6 = set(['bia', 'elena', 'fabio', 'gabriel', 'helio'])
inter = set(['duda', 'fabio', 'ilma', 'joão', 'katia', 'luiza'])

#%% ___a)
print(f'Os clientes do Banco Nubank são: {nubank}')
print(f'Os clientes do Banco C6 são: {c6}')
print(f'Os clientes do Banco Inter são: {inter}')

#%% ___b)
todos_clientes = nubank | c6 | inter
print(f'todos os clientes são:{todos_clientes}')

#%%___c)
NuC6 = nubank & c6
print(f'Os clientes que são dos dois bancos: {NuC6}')

#%%___d)
NuIn = nubank & inter
print(f'Os clientes que são dos dois bancos: {NuIn}')

#%%___e)
C6In = c6 & inter
print(f'Os clientes que são dos dois bancos: {C6In}')

#%%___f)
snubank = nubank - c6 - inter
print(f'cliente somente do Nubank: {snubank}')

#%%___g)
sc6 = c6 - nubank - inter
print(f'cliente somente do C6: {sc6}')

#%%__h)
sinter = inter - nubank - c6
print(f'cliente somente do Inter: {sinter}')

#%%__i)
print(f'Clientes somente do Nubank: {snubank}, e os clentes somente do C6 {sc6}')

#%%__j)
print(f'Clientes somente do Nubank: {snubank}, e os clentes somente do Inter {sinter}')

#%%__k)
print(f'Clientes somente do C6: {sc6}, e os clentes somente do Inter {sinter}')

#%%__l)
todos = nubank & c6 & inter
print(f'Os clientes dos tres bancos: {todos}')
# %%
