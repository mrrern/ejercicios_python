###
# 04 - Listas: Metodos
# metodos mas importantes para operar en las listas
###
print("\nLista inicial")
lista_abc = ["a", "b", "c"]
print(lista_abc)



'''
Agregar elementos
'''
print("\nAgregar al final un elemento")
lista_abc.append('d')
print(lista_abc)

#agregar un elemento en cierta posicion
print("\nAgregar en una posicion especifica un elemento")
lista_abc.insert(3, '@')
lista_abc.insert(5, '@')
print(lista_abc)


#agregar un elemento en el final
print("\nAgregar un elemento al final de la fila(extender)")
lista_abc.extend('e')
print(lista_abc)


'''
Eliminar elementos
'''

#eliminar la primera aparicion de un elemento
print("\nEliminar la primera aparicion del elemento")
lista_abc.remove('@')
print(lista_abc)

#eliminar el ultimo elemento
print("\nEliminar el ultimo elemento de una lista")
lista_abc.pop()
print(lista_abc)


#eliminar un elemento en una posicion especifica
print("\nEliminar el segundo elemento")
lista_abc.pop(3)
print(lista_abc)



#eliminar un elemento a lo bestia
print("\nEliminar un elemento de forma destructiva")
del lista_abc[3]
print(lista_abc)


#eliminar todos los elementos
#print("\nEliminar toda la lista")
#lista_abc.clear()
#print(lista_abc)


#eliminar un rango de elementos
print("\nEliminar un rango de elementos") 
del lista_abc[1:2]
print(lista_abc)


'''
metodos utiles en listas
'''
numbers = [1,6,3,100,5,98,7,8]

print("\n Ordenar elementos") 
#numbers.sort()
print(numbers)



#ordernar una lista creando una lista nueva
print("\n Ordener elementos creando otra lista") 

numeros_ordenados = sorted(numbers)
print(numeros_ordenados)


## 
numbers.append(3)
numbers.append(4)
numbers.append(5)
numbers.append(5)
numbers.append(5)


frutas = ['manzana', 'pera', 'zarrapia','cambur', 'ocumo', 'tomate']


#ordernar una cadenas de texto (minusculas)
print("\n Ordener elementos creando otra lista") 
frutas.sort(key=str.lower)
print(frutas)




#ordernar una cadenas de texto (Mezcla, mayuscula y minuscula)
frutas.append('Limon')
frutas.append('Pera')

print("\n Ordener elementos creando otra lista") 
frutas.sort(key=str.lower)
print(frutas)


#operaciones utiles con listas
print("\n Saber la longitud de una lista") 
print(len(numbers)) # len sirve para medir la longitud de una lista
print(numbers.count(5)) # count nos muestra cuantas veces se repite un elemento en una lista
print('zarrapia' in frutas) # in busca elementos dentro de la lista 
print(2000 in numbers) # y te devuelve un valor booleano

