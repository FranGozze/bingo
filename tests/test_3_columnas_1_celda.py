from src import bingo

mi_carton= bingo.carton()

def test_tres_columnas_una_celda():
    assert bingo.tres_columnas_una_celda(mi_carton)
    