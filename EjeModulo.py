#Crear un aplicativo matematico que el usuario pueda

import math

#raiz, algo con pi, redondear

x=int(input("Ingresa un numero para buscar la raiz cuadrada: "))
raiz= math.sqrt(x)
print(f'La raiz de {x} es: {raiz}')

v=int(input("Ingresa un numero para multiplicar por pi: "))
pi=round(math.pi,2)
print(f"El valor de pi multiplicado por {v} es: {pi*v}")


e=round(math.e,3)
print(f"El valor de redondeo es: {e}")

