import random
import string


def generar_contrasena(longitud, incluir_caracteres_especiales):
    caracteres = string.ascii_letters + string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena


def solicitar_opciones():
    longitud = int(input("Longitud de la contraseña: "))
    incluir_especiales = input(
        "¿Incluir caracteres especiales? (s/n): ").lower() == 's'
    return longitud, incluir_especiales


def main():
    print("Generador de contraseñas seguras")
    print("--------------------------------")

    longitud, incluir_especiales = solicitar_opciones()
    contrasena = generar_contrasena(longitud, incluir_especiales)

    print("\nContraseña generada:")
    print(contrasena)


if __name__ == '__main__':
    main()
