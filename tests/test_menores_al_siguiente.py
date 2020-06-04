from src import bingo

mi_carton= bingo.crear_carton()
def test_menores_al_siguente ():
    assert bingo.numeros_menores_al_siguiente (mi_carton)
