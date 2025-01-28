palabra=input("Ingrese la palabra:")
vocales="aeiouAEIOU"
contador=0

for letra in palabra:
    if letra in vocales:
        contador+=1

print(f"El numero de vocales es: {contador}")