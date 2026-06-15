###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###
print("Condicionales compuestas")

edad = int(input('Dame tu edad: '))

if edad >= 16: #Esta condicional es para evaluar si estamos en edad de tener licencia
    licencia_de_conducir = input('Tienes licencia de conducir? (si/no): ')
else:
    licencia_de_conducir = False

if licencia_de_conducir == "si": #En caso de decir si entonces la variable la volvemos True
    licencia_de_conducir = True
else:
    licencia_de_conducir = False
    
if edad >= 16 and licencia_de_conducir == True:
    print('Puedes conducir')
else:
    print('No puedes conducir')

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
# En JavaScript: 
# && sería and
# || sería or

name = input('Dame tu nombre: ')
apellido = input('dame tu apellido: ')
edad = input('dame tu edad: ')

if type(edad) != int:
    edad = 0
else:
    edad = int(edad)
    
if name != '' or apellido != '' or edad != 0:
    print(f'nombre {name}, apellido {apellido}, edad {edad}')
else:
    print('No proporcionaste todos los datos')
