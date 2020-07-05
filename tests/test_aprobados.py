from src import bingo

mi_carton= bingo.crear_carton()

def test_tres_columnas_una_celda():
    assert bingo.tres_columnas_una_celda(mi_carton)

def test_cinco_celdas_por_fila():
    assert  bingo.cinco_celdas_por_fila(mi_carton)

def test_no_menor_de_15():
    assert bingo.contar_celdas_ocupadas( mi_carton ) > 14
def test_no_mayor_de_15():
    assert bingo.contar_celdas_ocupadas( mi_carton) <16

def test_columna_orden_de_10():
    assert bingo.columna_orden_de_10(mi_carton)

def test_columnas_no_vacias():
    assert bingo.columnas_no_vacias( mi_carton  )

def test_columnas_sin_tres_celdas():
    assert bingo.columnas_sin_tres_celdas(mi_carton)

def test_filas_no_vacias():
    assert bingo.filas_no_vacias( mi_carton )

def test_numeros_menores_arriba():
    assert bingo.numeros_menores_arriba(mi_carton)

def test_no_mas_de_2_celdas_vacias_juntas():
    assert bingo.no_mas_de_2_celdas_vacias_juntas(mi_carton)

def test_numeros_no_repetidos():
    assert bingo.numeros_no_repetidos(mi_carton)

def test_no_mas_de_2_celdas_juntas():
    assert bingo.no_mas_de_2_celdas_juntas(mi_carton)

def  test_Numeros_1_a_90():
    assert bingo.numeros_1_a_90(mi_carton)

def test_matriz_de3x9():
    assert bingo.matriz_de_3x9(mi_carton)