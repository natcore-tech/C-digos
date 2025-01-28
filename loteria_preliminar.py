def es_periodico_decimal_puro(numero):
    # Un número es periódico decimal puro si es divisible por 3 y su resultado no es un entero
    return numero % 3 == 0 and (numero / 3) % 1 != 0

def main():
    while True:
        print("Bienvenido al juego de lotería")
        
        # Solicitar al jugador cuántos números desea ingresar
        cantidad_billetes = int(input("¿Cuántos números de billete deseas comprar? (1-100): "))
        
        # Validar que la cantidad de billetes esté en el rango permitido
        if cantidad_billetes < 1 or cantidad_billetes > 100:
            print("Por favor, ingresa una cantidad válida entre 1 y 100.")
            continue
        
        numeros = []
        for _ in range(cantidad_billetes):
            numero = int(input("Ingresa un número de billete (1-100): "))
            if 1 <= numero <= 100:
                numeros.append(numero)
            else:
                print("Número fuera de rango. Debe estar entre 1 y 100.")
        
        # Inicializar premios
        premio_mayor_ganado = False
        premio_1_ganado = False
        premio_2_ganado = False
        premio_3_ganado = False
        
        # Comprobar los números ingresados
        for numero in numeros:
            if numero == 23 and not premio_mayor_ganado:
                print(f"¡El número {numero} ha ganado el premio mayor!")
                premio_mayor_ganado = True
            elif es_periodico_decimal_puro(numero) and not premio_1_ganado:
                print(f"¡El número {numero} ha ganado el primer premio!")
                premio_1_ganado = True
            elif numero % 85 == 0 and not premio_2_ganado:
                print(f"¡El número {numero} ha ganado el segundo premio!")
                premio_2_ganado = True
            elif numero % 2 != 0 and str(numero).endswith('9') and not premio_3_ganado:
                print(f"¡El número {numero} ha ganado el tercer premio!")
                premio_3_ganado = True
        
        # Preguntar al jugador si desea jugar de nuevo
        jugar_de_nuevo = input("¿Deseas jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()