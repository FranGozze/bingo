from src import bingo

mi_carton= bingo.crear_carton()

def test_tres_columnas_una_celda():
    assert bingo.tres_columnas_una_celda(mi_carton)
    