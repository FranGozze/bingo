from src import bingo

mi_carton = bingo.crear_carton()

def test_columna_orden_de_10():
    assert bingo.columna_orden_de_10(mi_carton)
