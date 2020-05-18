
# Los 0 representan celdas vacias en el carton.
# Los 1 representan celdas ocupadas en el carton.

def carton():
    carton = (
        (0,11,0,32,44,0,62,73,0),
        (8,0,25,38,0,56,0,0,80),
        (0,17,29,0,47,0,67,0,88)
    )
    return carton

def contar_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda > 0:
                contador += 1
    return contador


def columnas_no_vacias(mi_carton):
    for i in range(9) :
        if not( mi_carton[0][i] or mi_carton[1][i] or mi_carton[2][i] ):  
                return False
    return True 

def filas_no_vacias(mi_carton):
    condicion = list((False, False, False))
    for i in range(3):
        for j in range(8):
            if( mi_carton[i][j]):
                condicion[i] = True
    
    return condicion[0] and condicion [1] and condicion[2]
def numeros_1_a_90(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if celda<0 or celda> 90:
                return False
    return True
def numeros_menores_arriba (mi_carton):
    for fila in range(9):
        if not(mi_carton[0][fila] <= mi_carton[1][fila]  or mi_carton[1][fila] == 0):
            return False
        if not(mi_carton[0][fila] <= mi_carton[2][fila] or mi_carton[2][fila] == 0): 
            return False
        if not(mi_carton[1][fila] <= mi_carton[2][fila] or mi_carton[2][fila] == 0):
            return False
    return True