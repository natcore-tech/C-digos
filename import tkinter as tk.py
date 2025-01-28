import tkinter as tk
from tkinter import messagebox

def perform_operation(operation):
    try:
        # Obtener las matrices de las entradas
        rows_a = int(rows_a_entry.get())
        cols_a = int(cols_a_entry.get())
        rows_b = int(rows_b_entry.get())
        cols_b = int(cols_b_entry.get())

        matrix_a = [[int(entry_a[i][j].get()) for j in range(cols_a)] for i in range(rows_a)]
        matrix_b = [[int(entry_b[i][j].get()) for j in range(cols_b)] for i in range(rows_b)]
        
        # Realizar la operación seleccionada
        if operation == "sumar":
            if rows_a != rows_b or cols_a != cols_b:
                messagebox.showerror("Error", "Las matrices deben tener las mismas dimensiones para sumar.")
                return
            result = [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols_a)] for i in range(rows_a)]
            operation_name = "Suma"
        elif operation == "restar":
            if rows_a != rows_b or cols_a != cols_b:
                messagebox.showerror("Error", "Las matrices deben tener las mismas dimensiones para restar.")
                return
            result = [[matrix_a[i][j] - matrix_b[i][j] for j in range(cols_a)] for i in range(rows_a)]
            operation_name = "Resta"
        elif operation == "multiplicar":
            if cols_a != rows_b:
                messagebox.showerror("Error", "El número de columnas de la matriz A debe ser igual al número de filas de la matriz B para multiplicar.")
                return
            result = [[sum(matrix_a[i][k] * matrix_b[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in range(rows_a)]
            operation_name = "Multiplicación"
        
        # Mostrar el resultado
        result_str = "\n".join(["\t".join(map(str, row)) for row in result])
        messagebox.showinfo("Resultado", f"{operation_name} de matrices:\n{result_str}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa solo números enteros.")

def create_matrix_entries():
    # Limpiar entradas anteriores
    for widget in matrix_a_frame.winfo_children():
        widget.destroy()
    for widget in matrix_b_frame.winfo_children():
        widget.destroy()

    # Crear entradas para la primera matriz
    rows_a = int(rows_a_entry.get())
    cols_a = int(cols_a_entry.get())
    global entry_a
    entry_a = [[None for _ in range(cols_a)] for _ in range(rows_a)]
    tk.Label(matrix_a_frame, text="Matriz A", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=cols_a)
    for i in range(rows_a):
        for j in range(cols_a):
            entry_a[i][j] = tk.Entry(matrix_a_frame, width=5)
            entry_a[i][j].grid(row=i+1, column=j, padx=5, pady=5)

    # Crear entradas para la segunda matriz
    rows_b = int(rows_b_entry.get())
    cols_b = int(cols_b_entry.get())
    global entry_b
    entry_b = [[None for _ in range(cols_b)] for _ in range(rows_b)]
    tk.Label(matrix_b_frame, text="Matriz B", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=cols_b)
    for i in range(rows_b):
        for j in range(cols_b):
            entry_b[i][j] = tk.Entry(matrix_b_frame, width=5)
            entry_b[i][j].grid(row=i+1, column=j, padx=5, pady=5)

# Crear la ventana principal
root = tk.Tk()
root.title("Operaciones con Matrices")

# Crear campos de entrada para las dimensiones de las matrices
tk.Label(root,