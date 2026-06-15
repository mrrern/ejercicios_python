###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###
print('Condicionales simples')
#cumplir requisitos
semestre = 3


#Estas son sentencias condicionales simples
if semestre == 1:
    print('Estoy comenzando mi semestre')
    print('Felicidades, eres un nuevo')

if semestre >= 2:
    print('Estas chiquito, pero ya sabes mas')


## Condicionales else/if
#Definimos una primera condicion if
# y  en caso de no cumplir la primera condicion
# se ejecutara el bloque de codigo de else

if semestre == 1:
    print('Estoy comenzando mi semestre')
    print('Felicidades, eres un nuevo')
elif semestre >= 2 and semestre <= 4:
    print('Estas en el intermedio del curso')
elif semestre >= 5 and semestre <= 8:
    print('Ya estas a mitad de carrera')
    print('Pero no te desanimes')
else: #Cuando no se cumple ninguna de las condiciones anteriores
    print('Que semestre es este?')
    print('Yo ya sali')