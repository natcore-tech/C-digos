
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []  

    def agregar_reserva(self, cliente, fecha, hora, numero_personas):
        for reserva in self.reservas:
            if reserva['fecha'] == fecha and reserva['hora'] == hora:
                print(f"Lo siento, ya hay una reserva a esa hora.")
                return
        nueva_reserva = {
            'cliente': cliente,
            'fecha': fecha,
            'hora': hora,
            'numero_personas': numero_personas
        }
        self.reservas.append(nueva_reserva)
        print(f"Reserva exitosa para {cliente} a las {hora} del {fecha} para {numero_personas} personas.")

    def cancelar_reserva(self, cliente, fecha, hora):
        for reserva in self.reservas:
            if reserva['cliente'] == cliente and reserva['fecha'] == fecha and reserva['hora'] == hora:
                self.reservas.remove(reserva)
                print(f"Reserva cancelada para {cliente} a las {hora} del {fecha}.")
                return
        print(f"No se encontró ninguna reserva para {cliente} a las {hora} del {fecha}.")

    def listar_reservas(self):
        if not self.reservas:
            print("No hay reservas actuales.")
        else:
            print(f"Reservas actuales en {self.nombre}:")
            for reserva in self.reservas:
                print(f"{reserva['cliente']} - {reserva['fecha']} {reserva['hora']} - {reserva['numero_personas']} personas")

    #def reporte_diario(self, fecha):
        reservas_del_dia = [reserva for reserva in self.reservas if reserva['fecha'] == fecha]
        if not reservas_del_dia:
            print(f"No hay reservas para el {fecha}.")
        else:
            print(f"Reporte de reservas para el {fecha}:")
            for reserva in reservas_del_dia:
                print(f"{reserva['cliente']} a las {reserva['hora']} - {reserva['numero_personas']} personas")

def menu():
    restaurante = Restaurante("La Buena Mesa")
    while True:
        print("\n--- Menú del Restaurante ---")
        print("  ---- La Buena Mesa ----")
        print("1. Agregar reserva")
        print("2. Cancelar reserva")
        print("3. Listar reservas")
        print("4. Generar reporte diario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            cliente = input("----------------\nNombre del cliente: ")
            fecha = input("-------------------\nFecha de la reserva (YYYY-MM-DD): ")
            hora = input("--------------------\nHora de la reserva (HH:MM): ")
            numero_personas = int(input("----------------\nNúmero de personas: "))
            restaurante.agregar_reserva(cliente, fecha, hora, numero_personas)
        
        elif opcion == '2':
            cliente = input("--------------\nNombre del cliente: ")
            fecha = input("----------------\nFecha de la reserva (YYYY-MM-DD): ")
            hora = input("------------------\nHora de la reserva (HH:MM): ")
            restaurante.cancelar_reserva(cliente, fecha, hora)
        
        elif opcion == '3':
            restaurante.listar_reservas()
        
        elif opcion == '4':
            fecha = input("---------------------------\nIngrese la fecha para el reporte (YYYY-MM-DD): ")
            restaurante.reporte_diario(fecha)
        
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elija de nuevo.")


menu()