import requests


def obtener_pares_disponibles():
    url = 'https://api.n.exchange/en/api/v1/pair/'
    response = requests.get(url)
    if response.status_code == 200:
        pares = response.json()
        return pares
    else:
        return None


def obtener_precio_mas_reciente(par):
    url = f'https://api.n.exchange/en/api/v1/price/{par}/latest/'
    response = requests.get(url)
    print(url)
    print(response.status_code)
    if response.status_code == 200:
        informacion_precio = response.json()
        return informacion_precio
    else:
        return None

