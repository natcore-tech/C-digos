# Función para pedir las notas al usuario
def registro_notas(Nnotas):
    notas = []
    Tnotas = 0
    print("\nLa nota ingresada debe ser entre 0 y 10.")
    
    for i in range(Nnotas):
        while True:
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                Tnotas += nota
                break
            else:
                print("Error: La nota debe ser entre 0 y 10. Intente nuevamente.")
    return notas, Tnotas

#Funcion para mostrar un resumen de los datos ingresados 
def mostrar_resumen(materia, notas, promedio):
    print(f"\nMateria: {materia}")
    print(f"Tus notas son: {notas}")
    print(f"Este es su promedio: {promedio:.2f}")
    
    if promedio >= 7:
        print("\n⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻")
        print(f"                 ¡Felicidades! Has aprobado {materia}.")
        print("⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼")
    else:
        print("\n⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻⊻")
        print(f"                  Lo siento, no has aprobado {materia}.")
        print("⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼⊼")

#Funcion donde pregunta si quiere el certificado de notas
def certificado(materia, promedio):
    import random
    import datetime
    n = random.randint(100, 999)
    hoy = datetime.date.today()
    fecha = hoy.strftime("%d/%m/%Y")
    print("")
    certi = input("¿Desea imprimir su certificado de notas? (Si/No): ")
    if certi == "si" or certi == "Si":
        print("\n...............................................................................")
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
        print("")
    elif certi == "no" or certi == "No":
        print("-------------------------------------------------------------------------------")
        print("Ok, no se generará el certificado.")
    else:
        print("Respuesta no válida. No se generará el certificado.")

def Promedio_Certificado():
    print("-------------------------------------------------------------------------------")
    materia = input("Introduzca el nombre de la materia: ")
    print("")
    Nnotas = int(input(f"¿Cuántas notas desea ingresar para {materia}? "))
    # Pedir notas y calcular el total de notas
    notas, Tnotas = registro_notas(Nnotas)
    # Calcular el promedio
    promedio = Tnotas / Nnotas
    # Mostrar resumen
    mostrar_resumen(materia, notas, promedio)
    # Preguntar si desea imprimir el certificado
    certificado(materia, promedio)