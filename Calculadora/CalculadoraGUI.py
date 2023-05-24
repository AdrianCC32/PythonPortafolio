import tkinter as tk


def sumar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="Resultado: " + str(resultado))


def restar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text="Resultado: " + str(resultado))


def multiplicar():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text="Resultado: " + str(resultado))


def dividir():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        resultado = num1 / num2
        label_resultado.config(text="Resultado: " + str(resultado))
    else:
        label_resultado.config(text="Error: División entre cero.")


# Crear ventana
window = tk.Tk()
window.title("Calculadora")

# Crear elementos de la interfaz
label_num1 = tk.Label(window, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

btn_sumar = tk.Button(window, text="Sumar", command=sumar)
btn_sumar.pack()

btn_restar = tk.Button(window, text="Restar", command=restar)
btn_restar.pack()

btn_multiplicar = tk.Button(window, text="Multiplicar", command=multiplicar)
btn_multiplicar.pack()

btn_dividir = tk.Button(window, text="Dividir", command=dividir)
btn_dividir.pack()

label_resultado = tk.Label(window, text="Resultado:")
label_resultado.pack()

# Ejecutar la ventana
window.mainloop()
