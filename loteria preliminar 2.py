while True:
        print(".......................................\nBienvenidos al mejor juego de loteria de Nayon!\n.......................................")
        nombre=input(f"Puedes ganar asombrosos premios\n''''''''''''''''''''''''''''''''''''\nPor favor para empezar ingresa tu nombre: ")
        print(f"-----------------------------\n{nombre} hay CUATRO PREMIOS\n------------------------------\nPrueba tu suerte y gana uno de los cuatro\n----------------------------")
        
        # Solicitar al jugador cuántos billetes va a ingresar
        cantidad_billetes = int(input("Ingresa el numero de boletos que has comprado: \n____________________________\nRECORDATORIOI: Si tu numero de boleto se repite, ganas una sola vez el premio\n_________________________________________________"))
        
        # Validar que la cantidad de billetes esté en el rango permitido
        if cantidad_billetes < 1 or cantidad_billetes > 100:
            print("Por favor, ingresa una cantidad válida entre 1 y 100\n////////////////\nIntentalo de nuevo\n///////////////")
            continue
        
        contador=0

        numeros = [] # Crea una lista vacia, paraq aginar valores despues
        for i in range(cantidad_billetes):
            numero = int(input(f"_________________________________\nPor favor ingresa el numero de tu boleto {i+1}: \n_______________________________________"))
            contador +=numero
            if 1 <= numero <= 100:
                numeros.append(numero)
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
                print(f"¡El número {numero} ha ganado el premio mayor!")
                print(f"!Te has ganado un CUPON DE COMIDA ILIMITADA DURANTE 3 DIAS")
                print("Si te llamas EMILY incluye un RAMO DE ORQUIDEAS")
                premio_mayor_ganado = True
            elif numero == 77 and not premio_2_ganado:
                print(f"¡El número {numero} ha ganado el segundo premio!")
                print(f"!Te has ganado una CITA CON MI HERMANO SI ERES MUJER\nCaso contrario una CITA CON MI PRIMA SI ERES HOMBRE")
                premio_2_ganado = True
            elif numero  % 8 == 0 and not premio_3_ganado:
                print(f"¡El número {numero} ha ganado el tercer premio!")
                print(f"!Te has ganado un PAQUETE DE GALLETAS OREO\nIncluye VASO DE LECHE VITA\n:D")
                premio_3_ganado = True
            elif numero % 12 == 0 and not premio_4_ganado:
                print(f"¡El número {numero} ha ganado el cuarto premio!")
                print(f"!Te has ganado un DORILOCO PICANTE\n")
                premio_4_ganado = True
        # Verificar si no se ganó ningún premio
        if not (premio_mayor_ganado or premio_2_ganado or premio_3_ganado or premio_4_ganado):
            print("Lo siento, no has ganado ningún premio. ¡Sigue intentando!")

        # Preguntar al jugador si desea jugar de nuevo
        jugar_de_nuevo = input("¿Deseas jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break # Se rompe el bucle 