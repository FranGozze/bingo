from src import bingo
mi_carton = bingo.crear_carton()
def test_columnas_no_vacias():
    assert bingo.columnas_no_vacias( mi_carton  )