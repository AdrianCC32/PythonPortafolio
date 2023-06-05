import statistics

def calcular_promedio(datos):
    return statistics.mean(datos)

def calcular_minimo(datos):
    return min(datos)

def calcular_maximo(datos):
    return max(datos)

def calcular_moda(datos):
    return statistics.mode(datos)
