### Tipos de Datos
## str: Todo dato que se escriba
## float: Numeros que tenga decimales
## int: Numeros enteros
## bool: true, false -> Son datos verdaderos o falsos
## list: Lista
## tuple: Lista  con con mas de una columna
## dict: Matriz(diccionario)
## set: asigna valores

print('Tipos de datos en python: ')

print("str: ")
print("Palabras: ") 
print(type("Palabras: ")) 


print('int: ')
print(43) #Estos datos son enteros
print(type(90)) #Estos datos son enteros
print(type(1)) #Estos datos son enteros
print(type(-1)) #Estos datos son enteros
print(type(30500)) #Estos datos son enteros


print('Aqui tenemos un float:')
print(43.2) #estos datos son numeros con decimales
print(type(43.2)) #estos datos son numeros con decimales


## Datos complejos

print("Vamos a definir una Lista")

frutas = [
    "Manzana",
    "Naranjas",
    "mora",
    "Uva",
    "Coroba"
]
print("Frutas")
 
print(frutas)

print("==================")
print("Vamos a definir una Tupla")

my_tuple = ("Richard Brito", 31)

print(my_tuple)

print("==================")
print("Vamos a definir un Set")

mi_nombre = {"Richard", 31}

print(mi_nombre)

print("==================")
print("Vamos a definir un Dic")

datos_personales = {"nombre" : "Richard", "apellido" : "Brito", "Edad" : 31}
print(datos_personales)

