numero=input("Ingrese el numero de loteria \nSu numero de loteria debe tener solo cuatro digitos: ")
loteria="56"

for ganador in numero:
    if numero in loteria:
        resultado="Felicitaciones su numero es el ganador"
    else:
        resultado="Su numero no es el ganador, siga participando"

print(f"{resultado}")
#condicionales, bucle, repetir para que vuelva a poder hacer
#rango del 1 al 100
#minimo 3 premios
#poder jugar minimo tres veces seguidas