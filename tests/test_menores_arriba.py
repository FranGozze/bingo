from src import bingo

mi_carton = bingo.carton()
def test_numeros_menores_arriba():
    assert bingo.numeros_menores_arriba(mi_carton)
