from src import bingo

mi_carton = bingo.crear_carton()

def test_no_mas_de_2_celdas_vacias_juntas():
    assert bingo.no_mas_de_2_celdas_vacias_juntas(mi_carton)