numeros=[3,9,8,1,4,5,3]
#sort ordena de menor a mayor
numeros.sort()
#len cuenta cuantos elementos hay en la lista
print("Aqui Len: ")
print(len(numeros))
#reverse cambia el sentido de la lista
numeros.reverse()
#count cuenta el elemento seleccionado el numero de veces que aparece
print(numeros.count(3))
#iterar es mostrar el contenido de la lista de forna mas ordenada
print("Inicio iterar")
for e in numeros:
    print(e)
print("Fin iterar")

print(numeros)
