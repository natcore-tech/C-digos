numero=int(input("Ingrese un numero: "))
if numero %2 ==0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

suma=0
for i in range(10):
    x=int(input(f"Ingrese el numero {i+1}: "))
    suma+=x