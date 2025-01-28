import random
import datetime

# Función para pedir las notas al usuario
def pedir_notas(materia, Nnotas):
    notas = []
    Tnotas = 0
    print("\nLa nota ingresada debe ser entre 0 y 10.")
    
    for i in range(Nnotas):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    Tnotas += nota
                    break
                else:
                    print("Error: La nota debe ser entre 0 y 10. Intente nuevamente.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")
    
    return notas, Tnotas

# Función para calcular el promedio
def calcular_promedio(Tnotas, Nnotas):
    return Tnotas / Nnotas

# Función para mostrar el resumen de los datos
def mostrar_resumen(materia, notas, promedio):
    print(f"\nMateria: {materia}")
    print(f"Tus notas son: {notas}")
    print(f"Este es su promedio: {promedio:.2f}")
    
    if promedio >= 7:
        print(f"¡Felicidades! Has aprobado {materia}.")
    else:
        print(f"Lo siento, no has aprobado {materia}.")

# Función para imprimir el certificado de notas
def certificado(materia, promedio):
    n = random.randint(100, 999)
    hoy = datetime.date.today()
    fecha = hoy.strftime("%d/%m/%Y")

    certi = input("\n¿Desea imprimir su certificado de notas? (Si/No): ")
    
    if certi == "si":
        print("|============================================================================|")
        print("|                    CERTIFICADO DE APROBACION DE MATERIA                    |")
        print("|============================================================================|")
        print("|                      NOMBRE DEL COLEGIO O UNIVERSIDAD                      |")
        print("|                           Departamento Academico                           |")
        print("|                               Quito, Ecuador                               |")
        print("|                                                                            |")
        print(f"|                            Certificado N° {n}                              |")
        print("|                                                                            |")
        print(f"|Fecha: {fecha}                                                           |")
        print("|                                                                            |")
        print("|----------------------------------------------------------------------------|")
        print("|                                                                            |")
        print(f"|Se certifica que el estudiante ha aprobado la materia:                      |\n|Materia: {materia}")
        print(f"|Promedio Final: {promedio:05.2f}                                                       |")
        print("|                                                                            |")
        print("|Por la presente se otorga este certificado al estudiante como reconocimiento|\n|de su desempeño académico.                                                  |")
        print("|                                                                            |")
        if promedio >= 6.99999999999999999:
            print("|¡Felicidades! El estudiante ha aprobado la materia con éxito.               |")
        else:
            print("|Lo sentimos, el estudiante no ha alcanzado el promedio mínimo para          |\n|aprobar la materia.                                                         |")
        print("|                                                                            |")
        print("|----------------------------------------------------------------------------|")
        print("|                                                                            |")
        print("|                           ______________________                           |")
        print("|                             Firma del profesor                             |")
        print("|============================================================================|")
    elif certi == "no":
        print("Ok, no se generará el certificado.")
    else:
        print("Respuesta no válida. No se generará el certificado.")

# Función principal que organiza todo el flujo
def main():
    materia = input("Introduzca el nombre de la materia: ")
    while True:
        try:
            Nnotas = int(input(f"¿Cuántas notas desea ingresar para {materia}? "))
            if Nnotas > 0:
                break
            else:
                print("Error: Debe ingresar un número positivo de notas.")
        except ValueError:
            print("Error: Debe ingresar un número válido para las notas.")
    
    # Pedir notas y calcular el total de notas
    notas, Tnotas = pedir_notas(materia, Nnotas)
    
    # Calcular el promedio
    promedio = calcular_promedio(Tnotas, Nnotas)
    
    # Mostrar resumen
    mostrar_resumen(materia, notas, promedio)
    
    # Preguntar si desea imprimir el certificado
    certificado(materia, promedio)
