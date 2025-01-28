#ingresar un numero para el bucle
#que se sume desde el 1 hasta el numero del bucle

#que me solicite cual quiero sumar si pares o impares
#que muesttre el resultado de la suma seleccionada

#solicitar el tamano del bucle
limite=int(input("Ingrese el tamano del bucle: "))
tipo=input("Ingrese si quiere PAR o IMPAR")
#iniciar con 0 la suma
suma=0
#crear el bucle
for i in range(1,limite+1):
    if tipo=="par"and i%2==0:
        suma+=i
        print(f"{suma-i} + {i} = {suma}")
    elif tipo=="impar"and i%2 !=0:
        suma+=i
        print(f"{suma-i} + {i} = {suma}")