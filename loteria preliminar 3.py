while True:
    print(".......................................\nBienvenidos al mejor juego de lotería de Nayon!\n.......................................")
    nombre = input(f"Puedes ganar asombrosos premios\n''''''''''''''''''''''''''''''''''''\nPor favor para empezar ingresa tu nombre: ")
    print(f"-----------------------------\n{nombre} hay CUATRO PREMIOS\n------------------------------\nPrueba tu suerte y gana al menos un premio\n--------------------------------")
    
    # Solicitar al jugador cuántos billetes va a ingresar
    cantidad_billetes = int(input("Ingresa el número de boletos que has comprado: "))
    
    # Validar que la cantidad de billetes esté en el rango permitido
    if cantidad_billetes < 1 or cantidad_billetes > 100:
        print("Por favor, ingresa una cantidad válida entre 1 y 100\n////////////////\nInténtalo de nuevo\n///////////////")
        continue
    
    contador = 0
    numeros = []  # Crea una lista vacía para acumular valores después
    numeros_registrados = set()  # Conjunto para almacenar números registrados, numeros no se pueden repetir`ss`

    for i in range(cantidad_billetes):
        while True:  # Bucle para asegurar que se ingrese un número válido
            numero = int(input(f"_________________________________\nPor favor ingresa el número de tu boleto {i + 1}: "))
            contador += numero
            
            if 1 <= numero <= 100:
                if numero in numeros_registrados:
                    print("************************************\nAdvertencia: El número ya fue registrado. Intenta con otro número.\n**************************************8*")
                else:
                    numeros.append(numero)
                    numeros_registrados.add(numero)  # Agregar el número al conjunto
                    break  # Salir del bucle si el número es válido y no se ha repetido
            else:
                print("Número fuera de rango\n/////////////////////\nDebe estar entre 1 y 100.\n/////////////////////")
    
    # Inicializar premios, variable booleana dos valores
    premio_mayor_ganado = False
    premio_2_ganado = False
    premio_3_ganado = False
    premio_4_ganado = False
    
    # Comprobar los números ingresados, condicionales
    for numero in numeros:
        if numero == 23 and not premio_mayor_ganado:
            print(f"¡El número {numero} ha ganado el premio mayor!\n................................")
            print(f"!Te has ganado un CUPON DE COMIDA ILIMITADA DURANTE 3 DÍAS\n.........................................")
            print("Si te llamas ALEJANDRO incluye un RAMO DE ORQUIDEAS\n....................................")
            premio_mayor_ganado = True
        elif numero == 77 and not premio_2_ganado:
            print(f"¡El número {numero} ha ganado el segundo premio!\n......................................")
            print(f"!Te has ganado una CITA CON MI HERMANO SI ERES MUJER\nCaso contrario una CITA CON MI PRIMA SI ERES HOMBRE\n....................................")
            premio_2_ganado = True
        elif numero % 8 == 0 and not premio_3_ganado:
            print(f"¡El número {numero} ha ganado el tercer premio!\n.................................")
            print(f"!Te has ganado un PAQUETE DE GALLETAS OREO\n.....................................\nIncluye VASO DE LECHE VITA :D\n...............................")
            premio_3_ganado = True
        elif numero % 12 == 0 and not premio_4_ganado:
            print(f"¡El número {numero} ha ganado el cuarto premio!\n............................")
            print(f"!Te has ganado un DORILOCO PICANTE\n.........................")
            premio_4_ganado = True
            
    # Verificar si no se ganó ningún premio
    if not (premio_mayor_ganado or premio_2_ganado or premio_3_ganado or premio_4_ganado):
        print("Lo siento, no has ganado ningún premio.\n...........................\n¡Pudes volver a intentarlo!")

    # Preguntar al jugador si desea jugar de nuevo
    jugar_de_nuevo = input("_______________________________\n¿Deseas jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo!= 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break # Se rompe el bucle 