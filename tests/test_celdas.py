from src.bingo import carton
from src.bingo import contar_celdas_ocupadas

mi_carton = carton()
def test_no_menor_de_15():
    assert contar_celdas_ocupadas( mi_carton ) > 14
def test_no_mayor_de_15():
    assert contar_celdas_ocupadas( mi_carton) <16
