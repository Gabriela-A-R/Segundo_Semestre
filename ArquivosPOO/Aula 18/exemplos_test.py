#a pasta e os arquivos devem ter o “test_*.py” ou “*_test.py”
 # instalar o pytest e execultar os testes: python -m pytest .\test_func.py
def soma_2(n):
    return n + 2

def test_1_numero_2():
    assert soma_2(2) == 4

def test_2_numero_3():
    assert soma_2(3) == 5

def test_3_numero_4():
    assert soma_2(4) == 4

def test_4_numero_5():
    assert soma_2(5) == 5


#%% EXPLICAÇÕES:
# ================================================ FAILURES ================================================ 
# ____________________________________________ test_3_numero_4 _____________________________________________ 

#     def test_3_numero_4():
# >       assert soma_2(4) == 4
# E       assert 6 == 4              ### Aqui mostra o que esta mostrando o resultado certo e o que eu esperava 
# E        +  where 6 = soma_2(4)

# exemplos_test.py:13: AssertionError
# ____________________________________________ test_4_numero_5 _____________________________________________ 

#     def test_4_numero_5():
# >       assert soma_2(5) == 5
# E       assert 7 == 5
# E        +  where 7 = soma_2(5)

# exemplos_test.py:16: AssertionError
# ======================================== short test summary info ========================================= 
# FAILED exemplos_test.py::test_3_numero_4 - assert 6 == 4
# FAILED exemplos_test.py::test_4_numero_5 - assert 7 == 5
# ====================================== 2 failed, 2 passed in 0.41s ======================================= 