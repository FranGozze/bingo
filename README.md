[![Build Status](https://travis-ci.com/FranGozze/bingo.svg?branch=master)](https://travis-ci.com/FranGozze/bingo) [![Coverage Status](https://coveralls.io/repos/github/FranGozze/bingo/badge.svg)](https://coveralls.io/github/FranGozze/bingo) 
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/FranGozze/bingo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/FranGozze/bingo/?branch=master)

# Bingo

Código en Python 3 que genera un cartón de bingo.
Escrito para Adaptación Del Ambiente De Trabajo, Instituto Politécnico Superior "Gral. San Martín", 2020, Prof. Mariano D'Agostino .

## Reglas
Se considara un cartón válido al que cumple con las siguientes condiciones:
* Cada carton es una matrix de 3 x 9.
* Los números del carton se encuentran en el rango 1 a 90.
* Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
* No hay números repetidos en el carton.
* Cada fila de un carton tiene exactamente 5 celdas ocupadas.
* Cada carton tiene 15 celdas ocupadas.
* Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
* No pueden existir columnas vacias.
* No pueden existir columnas con sus tres celdas ocupadas.
* Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
* En una fila no existen más de dos celdas vacías consecutivas.
* En una fila no existen más de dos celdas ocupadas consecutivas.

## Descarga
Para clonar el repositorio:
```
git clone https://github.com/eugeniobergia/bingo.git
```
Como requisito deberemos instalar `jinja2`. Para hacerlo:
```
pip install jinja2
```
Nota: para distribuciones basadas en Debian utilizar `pip3`

## Uso
Para generar un cartón por consola:
```
python bingo_print.py
```
Para generar un html con un cartón visual:
```
python bingo_html.py
```
Nota: para distribuciones basadas en Debian utilizar `python3`

Para más información sobre cómo instalar o actualizar Python visite https://www.python.org/

## Ejemplo de salida
### Consola
```
$ python3 bingo_print.py
[4, 0, 27, 31, 0, 52, 0, 0, 84]
[0, 0, 28, 33, 0, 59, 0, 71, 87]
[7, 15, 0, 0, 45, 0, 68, 78, 0]

```
### Web
```
$ python3 bingo_html.py
Generado "bingo.html".
```
![Ejemplo Bingo Web](https://github.com/FranGozze/bingo/blob/master/Imagenes/Ejemplo_de_carton_web.jpeg)
