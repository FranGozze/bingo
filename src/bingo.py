import math
import random
# Los 0 representan celdas vacias en el carton.
# Los 1 representan celdas ocupadas en el carton.
    
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


def numeros_no_repetidos(mi_carton):
    aux= []
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                aux.append(celda)
    if len(aux) !=  len(set(aux)):
        return False

    return True

def cinco_celdas_por_fila(mi_carton):
    
    for fila in mi_carton:
        sum=0
        for celda in fila:
            if celda > 0:
                sum += 1
        if sum != 5:
           return False

    return True

def tres_columnas_una_celda(mi_carton):
    
    sum=0
    for columna in range(9):
        contador=0
        if mi_carton[0][columna] > 0:
            contador +=1
        if mi_carton[1][columna] > 0:
            contador +=1
        if mi_carton[2][columna] > 0:
            contador +=1
        if contador == 1:
            sum +=1
    
    if sum == 3 :
        return True
    return False

def columnas_sin_tres_celdas(mi_carton):

    for columna in range(9):
        contador=0
        if mi_carton[0][columna] > 0:
            contador +=1
        if mi_carton[1][columna] > 0:
            contador +=1
        if mi_carton[2][columna] > 0:
            contador +=1
        if contador == 3:
            return False

    return True

def no_mas_de_2_celdas_juntas(mi_carton):
    
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda > 0 :
                contador += 1
            else:
                contador = 0
            if contador == 3 :
                return False
  
    return True

def no_mas_de_2_celdas_vacias_juntas(mi_carton):

    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda == 0 :
                contador += 1
            else:
                contador = 0
            if contador == 3 :
                return False
  
    return True

def columna_orden_de_10(mi_carton):
    mini = [1,10,20,30,40,50,60,70,80]
    maxi = [9,19,29,39,49,59,69,79,90]

    for x in range(3):
        for y in range(9):
            if mi_carton[x][y] != 0:
                if not (mi_carton[x][y] >= mini[y] and mi_carton[x][y] <= maxi[y]):
                    return False
    return True

def matriz_de_3x9(mi_carton):
    if len(mi_carton) != 3:
        return False
    for fila in mi_carton:
        if len(fila) != 9:
            return False

    return True





def intento_carton():
    contador = 0
    mi_carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton  < 15:
        contador += 1
        if (contador == 50):
            return intento_carton()

        numero = random.randint(1, 90)

        columna =int( math.floor (numero / 10))
        if (columna == 9):
             columna = 8
        huecos = 0
        for i in range(3) :
            if mi_carton[i][columna] == 0:
                huecos+=1
            if (mi_carton[i][columna] == numero):
                huecos = 0
                break
        if (huecos < 2):
            continue
        

        fila = 0
        for j in range(3):
            huecos = 0
            for i in range(9):
                if (mi_carton[fila][i] == 0):
                      huecos+=1
                

            if (huecos < 5 or mi_carton[fila][columna] != 0):
                fila+=1
            else:
                break
            
    
        if (fila == 3):
            continue
        

        mi_carton[fila][columna] = numero
        numerosCarton+=1
        contador = 0
        

    for x in range(9):
        huecos = 0
        for y in range(3) :
            if (mi_carton[y][x] == 0): 
                 huecos+=1
        
        if (huecos == 3):
            return intento_carton()
        
        

    return mi_carton

def crear_carton():
    while True:
        mi_carton = intento_carton()
        if(contar_celdas_ocupadas(mi_carton) == 15
        and cinco_celdas_por_fila(mi_carton)
        and filas_no_vacias(mi_carton)
        and columnas_no_vacias(mi_carton)
        and numeros_1_a_90(mi_carton)
        and numeros_menores_arriba(mi_carton)
        and numeros_no_repetidos(mi_carton)
        and columnas_sin_tres_celdas(mi_carton)
        and no_mas_de_2_celdas_juntas(mi_carton)
        and no_mas_de_2_celdas_vacias_juntas(mi_carton)
        and tres_columnas_una_celda(mi_carton)
        and matriz_de_3x9(mi_carton)
        and columna_orden_de_10(mi_carton)):
            return mi_carton
        
