###
# 03 - Cast de Datos
# Transformar un tipo de dato a otro

## float: Numeros que tenga decimales
## int: Numeros enteros
## bool: true, false -> Son datos verdaderos o falsos
###



print("Conversion de datos")

#Convertir cadenas de texto en Enteros
print(2 + int("100"))
print(type(int("23")))

print("==========")

#Convertir numeros en Cadenas de texto
print("El numero es " + str(100))
print(type("El numero es " + str(100)))

print("==========")
#Conversion de numeros decimales
print(float("3.1416"))
print(type(float("3.1416")))


print("==========")
#Redondear decimales
#el redondeo de decimales es con la funcion round()
print(int(3.62))

print(round(3.5))

print("==========")
#evaluar datos booleanos
print(bool(-1))
print(bool(""))
print(bool(" "))
print(bool("False"))

# para evaluar tipo de datos hacemos print(type(el dato que quiero evaluar))