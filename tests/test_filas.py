from src import bingo
mi_carton = bingo.crear_carton()
def test_filas_no_vacias():
    assert bingo.filas_no_vacias( mi_carton )
