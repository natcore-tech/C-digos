import random
import string
import Proyecto2_Parte2

users = {} #users.contra

def gen(length=8): #contra
    carac = string.ascii_letters + string.digits + string.punctuation
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
    
def admin(): #Dos
    ua="Natcore"
    ca="Coral2024"
    u=input("Introduce tu usuario de administrador: ")
    print("--------------------------------------------")
    c=input("Introduce tu contrasena de administrador: ")
    if ua == u and ca==c:
        print("---------------\nBienvenido Natcore\n----------------")
        print("Estos son lo usuarios y contraseñas que han sido registrados")
        print(users)
    else:
        print("Nombre de usuario o contraseña incorrectos")

def recu():
    nusu=input("Ingresa tu usuario para recuperar la contraseña: ")
    if nusu in users:
        print(f"----------------------\nTu contraseña es: {users[nusu]}")


def Login_PromedioYCertificado():
    print("")
    print("           ¡Bienvenidos al programa de registro y certificación!")
    print("\nEste espacio está diseñado para ayudarte a obtener tu certificado calculando \ntu promedio de notas de forma sencilla y rápida.")
    print("Solo necesitas registrarte y proporcionar tus calificaciones \nY nosotros nos encargamos de generar tu promedio.")
    print("\n                                ¡Comencemos!")
    while True:
        print("-------------------------------------------------------------------------------")
        print("1. Registro (estudiantes)")
        print("2. Iniciar sesión (estudiantes)")
        print("3. Iniciar sesion (docente)")
        print("4. Recuperar contraseña (estudiantes)")
        print("5. Salir")
        print("-------------------------------------------------------------------------------")
        opcion = input("Elige una opción: ")
        print("-------------------------------------------------------------------------------")
        if opcion == '1':
            reg()
        elif opcion == '2':
            iniciar = log()
            if iniciar:
                Proyecto2_Parte2.Promedio_Certificado()
        elif opcion == '3':
            admin()
        elif opcion== '4':
            recu()
        elif opcion == '5':
            print("Saliendo del programa..... \n")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

Login_PromedioYCertificado()
