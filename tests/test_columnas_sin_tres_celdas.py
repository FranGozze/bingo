from src import bingo

mi_carton = bingo.carton()

def test_columnas_sin_tres_celdas():
    assert bingo.columnas_sin_tres_celdas(mi_carton)