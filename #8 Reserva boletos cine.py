#Registro y usuario, menú
import string
import random

users = {} #users.contra

def gen(length=8): #contra
    carac = string.ascii_letters + string.digits
    return ''.join(random.choice(carac) for _ in range(length))

def reg(): #sign 
    if len(users) >= 5:
        print("No se pueden resgistrar mas usuarios. Limite alcanzado")
        return

    nom = input("Introduce tu nombre: ")
    if nom in users:
        print(f"El nombre de usuario ya está registrado.")
    else:
        contra = gen()
        users[nom] = contra
        print(f"Usuario registrado con éxito. Tu contraseña es: {contra}")

def log(): #login
    nom = input("Introduce tu nombre: ")
    print("----------------------------")
    contra = input("Introduce tu contraseña: ")

    if nom in users and users[nom] == contra:
        print("\nInicio de sesión exitoso.")
        return nom
    else:
        print("\nNombre de usuario o contraseña incorrectos.")
        return None

def menú():
    while True:
        print("-------------------------------------------------------------------------------")
        print("Bienvenido a Cinenat")
        print("Por favor inicia sesion o crea tu cuenta para darte un mejor servicio")
        print("1. Iniciar sesion")
        print("2. Crear cuenta")
        print("3. Peliculas disponibles")
        print("4. Salir")
        print("-------------------------------------------------------------------------------")
        opcion = input("Elige una opción: ")
        print("-------------------------------------------------------------------------------")
        if opcion == '1':
            log()
        elif opcion == '2':
            reg()
        elif opcion == '3':
            print("Elegiste 3")
        elif opcion== '4':
            print("Hasta la vista baby")
            print("-------------------------------------------------------------------------------")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

menú()