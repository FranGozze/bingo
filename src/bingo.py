
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
    for columna in range(9):
        if not(mi_carton[0][columna] <= mi_carton[1][columna]  or mi_carton[1][columna] == 0):
            return False
        if not(mi_carton[0][columna] <= mi_carton[2][columna] or mi_carton[2][columna] == 0): 
            return False
        if not(mi_carton[1][columna] <= mi_carton[2][columna] or mi_carton[2][columna] == 0):
            return False
    return True

def numeros_menores_al_siguiente (mi_carton):
    for fila in range(3):
        for columna in range(9):
            if mi_carton[fila][columna] != 0:
                for i in range(columna + 1, 9):
                    if mi_carton[0][i] != 0:
                        if mi_carton[0][i] < mi_carton[fila][columna]:
                            return False
                    if mi_carton[1][i] != 0:
                        if mi_carton[1][i] < mi_carton[fila][columna]:
                            return False
                    if mi_carton[2][i] != 0:
                        if mi_carton[2][i] < mi_carton[fila][columna]:
                            return False
    
            
    return True

def numeros_no_repetidos(mi_carton):
    aux= []
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                aux.append(celda)
    if len(aux) !=  len(set(aux)):
        return False

    return True
            