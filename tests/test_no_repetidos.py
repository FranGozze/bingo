from src import bingo
mi_carton = bingo.carton()
def test_numeros_no_repetidos():
    assert bingo.numeros_no_repetidos(mi_carton)