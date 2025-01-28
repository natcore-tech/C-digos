while True:
    print(".......................................\nBienvenido al LOTO COMELÓN!\n.......................................")
    nombre = input(f"Puedes ganar asombrosos premios\n''''''''''''''''''''''''''''''''''''\nPor favor para empezar ingresa tu nombre: ")
    print(f"-----------------------------\n{nombre} hay CUATRO PREMIOS\n------------------------------\nPrueba tu suerte y GANA al menos un PREMIO\n--------------------------------")
    print("Premios posibles: \n- Cupon comida ilimitada por 3 dias\n- Una cita con mi hermano o mi prima\n- Un paquete de galletas oreo\n- Doriloco Picante\n-----------------------------------------")
    
    # Boletos que ingresan
    canti = int(input("Ingresa el número de boletos que has comprado: "))
    
    # Boleto dentro del rango
    if canti < 1 or canti > 100:
        print("Por favor, ingresa una cantidad válida entre 1 y 100\n////////////////\nInténtalo de nuevo\n///////////////")
        continue
    
    contador = 0
    numeros = []  # Crea una lista 
    numre = set()  # Conjunto 

    for i in range(canti):
        while True:  # Bucle 
            numero = int(input(f"_________________________________\nPor favor ingresa el número de tu boleto {i + 1}: "))
            contador += numero
            
            if 1 <= numero <= 100:
                if numero in numre:
                    print("***********************************************\nAdvertencia: El número ya fue registrado. Intenta con otro número.\n********************************************")
                else:
                    numeros.append(numero)
                    numre.add(numero)  
                    break  
            else:
                print("Número fuera de rango\n^^^^^^^^^^^^^^^^^^^^^\nDebe estar entre 1 y 100.\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    
    # Dar valor 
    premio1 = False
    premio2 = False
    premio3 = False
    premio4 = False
    
    # Condicionales
    for numero in numeros:
        if numero == 23 and not premio1:
            print(f"¡Tu numero ha ganado el premio mayor!\n................................")
            print(f"!Te has ganado un CUPON DE COMIDA ILIMITADA DURANTE 3 DÍAS")
            print("Si te llamas ALEJANDRO incluye un RAMO DE ORQUIDEAS\n....................................")
            premio1 = True
            break
        elif numero %8 == 0 and not premio2:
            print(f"¡Tu numero ha ganado el segundo premio!\n--------------------------------------------------------")
            print(f"!Te has ganado una CITA CON MI HERMANO SI ERES MUJER\nCaso contrario una CITA CON MI PRIMA SI ERES HOMBRE\n-------------------------------------------------")
            premio2 = True
            break
        elif numero == 59 and not premio3: 
            print(f"¡Tu numero ha ganado el tercer premio!\n====================================================")
            print(f"!Te has ganado un PAQUETE DE GALLETAS OREO\nIncluye VASO DE LECHE VITA :D\n===========================================")
            premio3 = True
            break
        elif numero == 99 and not premio4: 
            print(f"¡Tu numero ha ganado el cuarto premio!\n________________________________________________")
            print(f"!Te has ganado un DORILOCO PICANTE\n__________________________________________")
            premio4 = True
            break

    # Si el no coincide no gana premio
    if not (premio1 or premio2 or premio3 or premio4):
        print("=====================================\nLo siento, NO GANASTE ningún PREMIO.\n========================================\n¡Puedes VOLVER A INTENTARLO!")

    # Bucle para repetir juego hasta que seleccione salir
    jugar = input("_______________________________\n¿Deseas jugar de nuevo? (s/n): ").lower()
    if jugar!= 's' :
            print("::::::::::::::::::::::::::::\nGracias por jugar. ¡Hasta la próxima!\n::::::::::::::::::::::::::::::::")
            break 