from src import bingo

mi_carton = bingo.crear_carton()

def  test_Numeros_1_a_90():
    assert bingo.numeros_1_a_90(mi_carton)
    