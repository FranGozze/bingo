from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    return contador

def test_no_menor_de_15():
       assert test_contar_celdas_ocupadas() > 14
def test_no_mayor_de_15():
        assert test_contar_celdas_ocupadas() <16
