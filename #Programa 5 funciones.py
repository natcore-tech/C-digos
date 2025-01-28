#Programa 5 funciones
#Verifica numero es par o impar
#Saludar a una persona
#Mayor de dos numeros
#Cantidad de vocales en una palabra
#grados celsius a fahrenheit
print("Bienvenido a este programa que ni entiendo")
print("1. Numero es par o impar")
print("2. Saludar a una persona")
print("3. Mayor de dos numeros")
print("4. Cantidad de vocales")
print("5. Grados celsius a farenheit")
entrada=input("Escoge una opcion: ")
if entrada is 1:
    def mayor(a,b):
        a=int(input("Por favor ingresa el primer numero: "))
        b=int(input("Por favor ingresa el segundo numero: "))
        if a>b:
            print(f"El numero {a} es mayor que {b}")
        elif a<b:
            print(f"El numero {b} es mayor que {a}")