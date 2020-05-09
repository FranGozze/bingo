from src.bingo import carton
from src.bingo import filas_no_vacias

def test_filas_no_vacias():
    assert filas_no_vacias( carton() )
