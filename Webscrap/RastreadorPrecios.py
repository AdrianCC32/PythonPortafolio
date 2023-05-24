import requests
from bs4 import BeautifulSoup
import smtplib


def obtener_precio(url):
    # Realizar la solicitud HTTP al sitio web
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar el elemento que contiene el precio
    precio = soup.find('span', class_='price').get_text()

    # Eliminar símbolos y espacios no deseados del precio
    precio_limpio = ''.join(
        c for c in precio if c.isdigit() or c in ['.', ','])
    precio_limpio = precio_limpio.replace(',', '.')

    return float(precio_limpio)


def enviar_notificacion(destinatario, mensaje):
    # Configurar el servidor SMTP para enviar el correo electrónico
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'correo@gmail.com'
    sender_password = 'contraseña'

    # Crear una conexión segura con el servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Enviar el correo electrónico
    server.sendmail(sender_email, destinatario, mensaje)

    # Cerrar la conexión con el servidor SMTP
    server.quit()


def main():
    # URL del producto que deseas rastrear
    url_producto = 'https://www.example.com/producto'

    # Precio umbral
    umbral_precio = 100.0

    # Dirección de correo electrónico para recibir notificaciones
    destinatario = 'correo@gmail.com'

    # Obtener el precio actual del producto
    precio_actual = obtener_precio(url_producto)

    if precio_actual < umbral_precio:
        mensaje = f'El precio del producto ha bajado a {precio_actual} USD. ¡Aprovecha la oferta!'
        enviar_notificacion(destinatario, mensaje)
    else:
        print('El precio del producto no ha alcanzado el umbral deseado.')


if __name__ == '__main__':
    main()
