from src import bingo

mi_carton = bingo.crear_carton()
def test_numeros_menores_arriba():
    assert bingo.numeros_menores_arriba(mi_carton)
