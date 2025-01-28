import string

# Imprimir todas las letras del alfabeto
print("Letras: ", string.ascii_letters)

# Imprimir todos los dígitos
print("Dígitos: ", string.ascii_lowercase)
print("Dígitos: ", string.octdigits)


# Imprimir todos los caracteres de puntuación
print("Puntuación: ", string.punctuation)

# Usar string.ascii_letters para generar una cadena aleatoria
import random

def generar_nombre_usuario(longitud=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(longitud))

usuario = generar_nombre_usuario()
print("Nombre de usuario generado: ", usuario)