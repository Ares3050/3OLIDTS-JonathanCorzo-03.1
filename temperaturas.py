import tkinter as tk
from tkinter import messagebox

def calcular_temperatura():
    entradas = [tbcelsius.get(), tbFahrenheit.get(), tbKelvin.get()]
    num_entradas = sum(bool(e.strip()) for e in entradas)

    if num_entradas == 0:
        messagebox.showwarning("Advertencia", "Ingrese un valor en una sola casilla.")
        return
    elif num_entradas > 1:
        messagebox.showwarning("Advertencia", "Ingrese solo un valor a la vez.")
        return

    try:
        if tbcelsius.get().strip():
            c = float(tbcelsius.get())
            f = (c * 9 / 5) + 32
            k = c + 273.15
        elif tbFahrenheit.get().strip():
            f = float(tbFahrenheit.get())
            c = (f - 32) * 5 / 9
            k = c + 273.15
        elif tbKelvin.get().strip():
            k = float(tbKelvin.get())
            c = k - 273.15
            f = (c * 9 / 5) + 32

        # Mostrar resultados
        tbcelsius.delete(0, tk.END)
        tbcelsius.insert(0, f"{c:.2f}")
        tbFahrenheit.delete(0, tk.END)
        tbFahrenheit.insert(0, f"{f:.2f}")
        tbKelvin.delete(0, tk.END)
        tbKelvin.insert(0, f"{k:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")

def limpiar_campos():
    tbcelsius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)
    tbKelvin.delete(0, tk.END)
    messagebox.showinfo("Limpiar", "Se han borrado los valores.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Temperaturas")
ventana.resizable(False, False)

# Marco de entrada
frame = tk.LabelFrame(ventana, text="Conversión de Temperaturas", padx=15, pady=15)
frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Etiquetas y entradas
tk.Label(frame, text="Celsius (°C)").grid(row=0, column=0, sticky="e")
tk.Label(frame, text="Fahrenheit (°F)").grid(row=1, column=0, sticky="e")
tk.Label(frame, text="Kelvin (K)").grid(row=2, column=0, sticky="e")

tbcelsius = tk.Entry(frame)
tbFahrenheit = tk.Entry(frame)
tbKelvin = tk.Entry(frame)

tbcelsius.grid(row=0, column=1, padx=10, pady=5)
tbFahrenheit.grid(row=1, column=1, padx=10, pady=5)
tbKelvin.grid(row=2, column=1, padx=10, pady=5)

# Botones
btnCalcular = tk.Button(ventana, text="Calcular", width=15, command=calcular_temperatura)
btnLimpiar = tk.Button(ventana, text="Limpiar", width=15, command=limpiar_campos)
btnSalir = tk.Button(ventana, text="Salir", width=15, command=ventana.quit)

btnCalcular.grid(row=1, column=0, pady=5)
btnLimpiar.grid(row=2, column=0, pady=5)
btnSalir.grid(row=2, column=1, pady=5)

ventana.mainloop()

