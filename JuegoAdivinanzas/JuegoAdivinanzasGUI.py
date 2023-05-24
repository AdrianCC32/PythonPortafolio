import random
import tkinter as tk


class JuegoAdivinanzas:
    def __init__(self, palabras):
        self.palabras = palabras
        self.palabra_oculta = random.choice(palabras).lower()
        self.intentos = 0
        self.letras_adivinadas = []

    def obtener_letras_adivinadas(self):
        letras = []
        for letra in self.palabra_oculta:
            if letra in self.letras_adivinadas:
                letras.append(letra)
            else:
                letras.append('_')
        return ' '.join(letras)

    def adivinar_letra(self, letra):
        letra = letra.lower()
        if letra in self.letras_adivinadas:
            return 'Ya has adivinado esa letra.'

        self.letras_adivinadas.append(letra)
        self.intentos += 1

        if letra in self.palabra_oculta:
            return f'¡Correcto! La letra "{letra}" está en la palabra. Palabra actual: {self.obtener_letras_adivinadas()}'
        else:
            return f'La letra "{letra}" no está en la palabra. Palabra actual: {self.obtener_letras_adivinadas()}'

    def ha_ganado(self):
        return set(self.palabra_oculta) == set(self.letras_adivinadas)


class JuegoAdivinanzasGUI:
    def __init__(self, palabras):
        self.juego = JuegoAdivinanzas(palabras)
        self.ventana = tk.Tk()
        self.ventana.title('Juego de Adivinanzas')

        self.palabra_actual_label = tk.Label(
            self.ventana, text='Palabra actual: ')
        self.palabra_actual_label.pack()

        self.letra_entry = tk.Entry(self.ventana)
        self.letra_entry.pack()

        self.adivinar_button = tk.Button(
            self.ventana, text='Adivinar', command=self.adivinar_letra)
        self.adivinar_button.pack()

        self.resultado_label = tk.Label(self.ventana, text='')
        self.resultado_label.pack()

        self.intentos_label = tk.Label(self.ventana, text='')
        self.intentos_label.pack()

        self.ventana.mainloop()

    def actualizar_palabra_actual(self):
        self.palabra_actual_label.config(
            text=f'Palabra actual: {self.juego.obtener_letras_adivinadas()}')

    def actualizar_intentos(self):
        self.intentos_label.config(text=f'Intentos: {self.juego.intentos}')

    def adivinar_letra(self):
        letra = self.letra_entry.get()
        resultado = self.juego.adivinar_letra(letra)
        self.resultado_label.config(text=resultado)

        if self.juego.ha_ganado():
            self.resultado_label.config(
                text=f'¡Felicidades! Has adivinado la palabra "{self.juego.palabra_oculta}" en {self.juego.intentos} intentos.')
            self.letra_entry.config(state='disabled')
            self.adivinar_button.config(state='disabled')

        self.actualizar_palabra_actual()
        self.actualizar_intentos()
        self.letra_entry.delete(0, tk.END)


def main():
    palabras = ['python', 'programacion',
                'computadora']
    juego_gui = JuegoAdivinanzasGUI(palabras)


if __name__ == '__main__':
    main()
