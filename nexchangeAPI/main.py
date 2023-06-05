import api_utils
import file_utils
import statistics_utils as statistics
import graphing


def mostrar_menu():
    print('--- Menú ---')
    print('1. Consultar información de la API')
    print('2. Leer información desde un archivo')
    print('3. Guardar información en un archivo')
    print('4. Análisis estadístico')
    print('5. Generar gráficas')
    print('0. Salir')


def obtener_opcion_usuario():
    opcion = input('Ingrese su elección: ')
    return opcion


def obtener_par_valido():
    pares_disponibles = api_utils.obtener_pares_disponibles()
    if pares_disponibles:
        pares_validos = [par['name'] for par in pares_disponibles]
        while True:
            par = input(
                'Ingrese el par de criptomonedas (por ejemplo, BTCLTC o ETHBTC): ')
            if par in pares_validos:
                return par
            else:
                print('Par de criptomonedas inválido. Intente nuevamente.')
    else:
        print('No se pudo obtener la lista de pares de criptomonedas.')


def consultar_datos_api():
    par = obtener_par_valido()
    if par:
        informacion_precio = api_utils.obtener_precio_mas_reciente(par)
        if informacion_precio:
            print(f'Último precio de {par}:' + informacion_precio[0]['rate'])
            eleccion = input(
                '¿Desea guardar la información consultada? (s/n): ')
            if eleccion.lower() == 's':
                nombre_archivo = input(
                    'Ingrese el nombre del archivo para guardar los datos: ')
                file_utils.escribir_datos_en_archivo(
                    informacion_precio, nombre_archivo)
                print('Datos guardados correctamente.')
        else:
            print('No se pudo obtener el precio.')
    else:
        print('Par de criptomonedas inválido.')


def leer_datos_desde_archivo():
    nombre_archivo = input(
        'Ingrese el nombre del archivo para leer los datos: ')
    datos = file_utils.leer_datos_desde_archivo(nombre_archivo)
    if datos:
        print('Datos leídos del archivo:')
        print(datos)
    else:
        print('No se encontró el archivo.')


def guardar_datos_api():
    par = obtener_par_valido()
    if par:
        informacion_precio = api_utils.obtener_precio_mas_reciente(par)
        if informacion_precio:
            datos = [{
                'par': par,
                'rate': informacion_precio[0]['rate']
            }]
            nombre_archivo = input(
                'Ingrese el nombre del archivo para guardar los datos: ')
            file_utils.escribir_datos_en_archivo(datos, nombre_archivo)
            print('Datos guardados correctamente.')
        else:
            print('No se pudo obtener el precio.')
    else:
        print('Par de criptomonedas inválido.')

def realizar_analisis_estadistico():
    nombre_archivo = input('Ingrese el nombre del archivo que contiene los datos: ')
    datos = file_utils.leer_datos_desde_archivo(nombre_archivo)
    if datos:
        precios = []

        for entrada in datos:
            if isinstance(entrada, dict):
                if 'rate' in entrada:
                    precios.append(float(entrada['rate']))
                elif 'precio' in entrada:
                    precios.append(float(entrada['precio']))
                else:
                    print('Campo inválido en el JSON.')
            else:
                print('El elemento no es un objeto JSON válido.')

        if len(precios) > 0:
            promedio = statistics.calcular_promedio(precios)
            minimo = statistics.calcular_minimo(precios)
            maximo = statistics.calcular_maximo(precios)
            moda = statistics.calcular_moda(precios)

            print('Análisis estadístico:')
            print(f'Promedio: {promedio}')
            print(f'Mínimo: {minimo}')
            print(f'Máximo: {maximo}')
            print(f'Moda: {moda}')
        else:
            print('No se encontraron datos válidos para realizar el análisis estadístico.')
    else:
        print('No se encontró el archivo.')




def generar_graficas():
    nombre_archivo = input(
        'Ingrese el nombre del archivo que contiene los datos: ')
    datos = file_utils.leer_datos_desde_archivo(nombre_archivo)
    if datos:
        precios = [entrada['rate'] for entrada in datos]
        fechas = [entrada['created_on'] for entrada in datos]

        graphing.graficar_diagrama_de_lineas(
            fechas, precios, 'Fechas', 'Precios', 'Gráfico de precios')
        graphing.graficar_diagrama_de_barras(
            fechas, precios, 'Fechas', 'Precios', 'Gráfico de barras')
        graphing.graficar_diagrama_de_pastel(
            fechas, precios, 'Gráfico de pastel')
    else:
        print('No se encontró el archivo.')


def main():
    while True:
        mostrar_menu()
        opcion = obtener_opcion_usuario()

        if opcion == '0':
            break
        elif opcion == '1':
            consultar_datos_api()
        elif opcion == '2':
            leer_datos_desde_archivo()
        elif opcion == '3':
            guardar_datos_api()
        elif opcion == '4':
            realizar_analisis_estadistico()
        elif opcion == '5':
            generar_graficas()
        else:
            print('Elección inválida. Intente nuevamente.')


if __name__ == '__main__':
    main()
