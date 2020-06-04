from src import bingo
mi_carton = bingo.crear_carton()
def test_no_menor_de_15():
    assert bingo.contar_celdas_ocupadas( mi_carton ) > 14
def test_no_mayor_de_15():
    assert bingo.contar_celdas_ocupadas( mi_carton) <16
