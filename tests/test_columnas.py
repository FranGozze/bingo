from src.bingo import carton

def test_columnas_no_vacias():
    mi_carton = carton()
    for i in range(9) :
        if not( mi_carton[0][i] or mi_carton[1][i] or mi_carton[2][i] ):  
                assert False
    assert True 