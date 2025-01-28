def resolver_sistema(ecuaciones):
    n = len(ecuaciones)
    
    # Aplicamos eliminación de Gauss
    for i in range(n):
        # Asegurarnos de que el pivote no sea cero
        if ecuaciones[i][i] == 0:
            for j in range(i + 1, n):
                if ecuaciones[j][i] != 0:
                    ecuaciones[i], ecuaciones[j] = ecuaciones[j], ecuaciones[i]
                    break

        # Hacer ceros debajo del pivote
        for j in range(i + 1, n):
            factor = ecuaciones[j][i] / ecuaciones[i][i]
            for k in range(i, n + 1):
                ecuaciones[j][k] -= factor * ecuaciones[i][k]

    # Resolver el sistema con sustitución hacia atrás
    solucion = [0] * n
    for i in range(n - 1, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += ecuaciones[i][j] * solucion[j]
        solucion[i] = (ecuaciones[i][n] - suma) / ecuaciones[i][i]

    return solucion

def main():
    # Pedir al usuario el número de ecuaciones
    n = int(input("Ingresa el número de ecuaciones: "))
    
    ecuaciones = []
    
    # Ingresar los coeficientes y las constantes
    for i in range(n):
        while True:  # Usamos un bucle para repetir en caso de error
            fila = list(map(float, input(f"Ingrese los coeficientes de la ecuación {i+1} (separados por espacio): ").split()))
            if len(fila) != n:  # Verificamos que la cantidad de coeficientes sea correcta
                print(f"Error: Debes ingresar exactamente {n} coeficientes para la ecuación {i+1}. Intenta nuevamente.")
            else:
                break  # Si todo está bien, salimos del bucle
        
        while True:  # Bucle para ingresar la constante
            try:
                constante = float(input(f"Ingrese la constante de la ecuación {i+1}: "))
                break  # Salimos del bucle si la constante es válida
            except ValueError:
                print("Error: Debes ingresar un número válido para la constante. Intenta nuevamente.")
        
        fila.append(constante)  # Agregamos la constante a la fila
        ecuaciones.append(fila)
    
    # Resuelve el sistema
    solucion = resolver_sistema(ecuaciones)
    
    # Imprime la solución
    print(f"La solución del sistema es: {solucion}")

main()
