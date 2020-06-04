from src import bingo
mi_carton = bingo.crear_carton()
def test_numeros_no_repetidos():
    assert bingo.numeros_no_repetidos(mi_carton)