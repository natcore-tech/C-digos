#Registro y usuario, menú

def reglog():
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
            print("Elegiste 1")
        elif opcion == '2':
            print("Elegiste 2")
        elif opcion == '3':
            print("Elegiste 3")
        elif opcion== '4':
            print("Hasta la vista baby")
            print("-------------------------------------------------------------------------------")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

reglog()