def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: División entre cero.")
        return None


def calcular():
    print("Calculadora Básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = int(
        input("Ingrese el número de la operación que desea realizar: "))

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == 1:
        resultado = sumar(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif operacion == 2:
        resultado = restar(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif operacion == 3:
        resultado = multiplicar(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif operacion == 4:
        resultado = dividir(num1, num2)
        if resultado is not None:
            print("El resultado de la división es:", resultado)
    else:
        print("Operación no válida.")


calcular()
