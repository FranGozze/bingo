from jinja2 import Template
from src.bingo import crear_carton

template = Template(open("plantilla_web/plantilla.j2").read())
file = open ("bingo.html" , "w")
file.write(template.render(carton= crear_carton()))
file.close()
print ("Generando \"bingo.html\".")