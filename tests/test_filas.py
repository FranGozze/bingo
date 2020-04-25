from src.bingo import carton

def test_filas_no_vacias():
    mi_carton=carton()
    condicion = list((False, False, False))
    for i in range(3):
        for j in range(8):
            if( mi_carton[i][j]):
                condicion[i] = True
    
    assert condicion[0] and condicion [1] and condicion[2]