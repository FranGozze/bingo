from src.bingo import carton
from src.bingo import columnas_no_vacias

def test_columnas_no_vacias():
    assert columnas_no_vacias( carton() )