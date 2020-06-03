from src import bingo
mi_carton=bingo.carton()

def test_cinco_celdas_por_fila():
    assert  bingo.cinco_celdas_por_fila(mi_carton)