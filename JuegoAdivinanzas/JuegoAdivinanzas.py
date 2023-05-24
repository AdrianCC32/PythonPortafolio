import random

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

def main():
    palabras = ['python', 'programacion', 'computadora', 'openai', 'inteligencia']
    juego = JuegoAdivinanzas(palabras)

    print('Bienvenido al juego de adivinanzas.')
    print('Adivina la palabra letra por letra.')
    print('-------------------------------')

    while True:
        print(f'Palabra actual: {juego.obtener_letras_adivinadas()}')
        letra = input('Ingresa una letra: ')
        resultado = juego.adivinar_letra(letra)
        print(resultado)
        print('-------------------------------')

        if juego.ha_ganado():
            print(f'¡Felicidades! Has adivinado la palabra "{juego.palabra_oculta}" en {juego.intentos} intentos.')
            break

    print('¡Juego terminado!')

if __name__ == '__main__':
    main()
