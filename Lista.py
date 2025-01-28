#Cual es la diferencia entre una lista, tupla y diccionario
lista=[1,2,3,4]
print(lista[0])
print(lista[-1])
print(lista[-2])

#append () agrega un elemento al final de la lista
lista.append(5)
#insert () agrega un elemento en una posición específica
lista.insert(1,10)
#remove () elimina un elemento de la lista
lista.remove(4)
#pop () elimina un elemento de la lista y lo devuelve
lista.pop(0)
#clear () elimina todos los elementos de la lista
lista.clear

print(lista)