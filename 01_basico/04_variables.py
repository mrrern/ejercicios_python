##
# 04 - Variables
# Guadar datos de usuario en la memoria
#
###

# asignamos una variable
name = 'Richard'
print('+++++++++++++ ') 
print('Nombre guardado:') 
print(name) 
print('+++++++++++++ ')
age = 31
print(age)
print('+++++++++++++ ') 
# al colocar la letra f antes de las comillas, estoy indicando quen en el texto puedo ingresar variables
print(f'Datos personales: Edad: {age} Nombre: {name}') # Estas comillas simples o dobles sirven para escribir de forma lineal
print(f"Datos personales: Edad: {age} Nombre: {name}") # Estas comillas simples o dobles sirven para escribir de forma lineal


print('+++++++++++++ ') 
##Si quiero colocar un valor mas largo de texto o que tenga saltos de linea puedo hacerlo con """ """ o ''' '''  
print(f''' 
Datos recolectados:
      Nombre : {name}
      edad : {age}
''')

print(''' 
Esto es un salto
de Linea
Para escribir en textos largos
''')

#nombres recomendables de variables
nombreDeMiVariable = "No recomendado" #camel case
MiNombreDeVariable = "No recomendada" #Pascal Case
minombredevarible = "No por favor" #todo junto


mi_nombre_de_variable= "ok" #snake case

MI_CONSTANTE = 3.14 #este es un valor constante


is_logged_in: bool = True # escribo una variable, defino su tipo de dato y defino el valor inicial
print(is_logged_in)

nombre: str = "Richard" # si coloco : es para definir el tipo de dato y si coloco = es para definir el