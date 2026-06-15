###
# 05 - Input
# funcion input() que lo que va a hacer es obtener datos del usuario
###

# print(''' 
# Esto es un salto
# de Linea
# Para escribir en textos largos
# ''')

#nombre = input("Escribe tu nombre: ")
#apellido = input("Escribe tu apellido: ")
ciudad = input("Escribe tu cuidad: ")

peso = input("Escribe tu peso aqui: ") 
altura = input("Escribe tu altura aqui: ")

altura_cuadrado = float(altura) * float(altura)
imc = float(peso) / altura_cuadrado


#print(f'Hola {nombre} {apellido}, como estas?')

print(f'Estas viviendo en Merida')

print(f'tu IMC es {imc}')




## Hagamos un formulario con los siguientes datos -> Nombre, apellido, ciudad en donde vives