from src import bingo

mi_carton= [
        [20,0,0,0,0,0,5,0,1],
        [2,0,0,10,0,0,0,1,100],
        [0,3,1,0,3,0,1,0,9]
    ] 

mi_carton1= [
        [1,1,1,1,2,1,5,0,1],
        [2,1,3,10,1,4,3,0,1],
        [0,0,0,0,0,0,0,0,0],
    ] 


def test_tres_columnas_una_celda():
    assert not bingo.tres_columnas_una_celda(mi_carton1) 

def test_cinco_celdas_por_fila():
    assert  not  bingo.cinco_celdas_por_fila(mi_carton1)

def test_no_menor_de_15():
    assert  not bingo.contar_celdas_ocupadas( mi_carton ) > 14
def test_no_mayor_de_15():
    assert  not (bingo.contar_celdas_ocupadas( mi_carton1) <16)

def test_columna_orden_de_10():
    assert not bingo.columna_orden_de_10(mi_carton)

def test_columnas_no_vacias():
    assert not bingo.columnas_no_vacias( mi_carton)

def test_columnas_sin_tres_celdas():
    assert not bingo.columnas_sin_tres_celdas(mi_carton)

def test_filas_no_vacias():
    assert not bingo.filas_no_vacias( mi_carton1 )

def test_numeros_menores_arriba():
    assert not bingo.numeros_menores_arriba(mi_carton)

def test_no_mas_de_2_celdas_vacias_juntas():
    assert not bingo.no_mas_de_2_celdas_vacias_juntas(mi_carton)

def test_numeros_no_repetidos():
    assert not bingo.numeros_no_repetidos(mi_carton)

def test_no_mas_de_2_celdas_juntas():
    assert not bingo.no_mas_de_2_celdas_juntas(mi_carton1)

def  test_Numeros_1_a_90():
    assert not bingo.numeros_1_a_90(mi_carton)
    