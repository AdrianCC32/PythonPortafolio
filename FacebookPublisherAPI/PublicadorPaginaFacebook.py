import os
import requests
from datetime import datetime
import schedule
import time

# Este script sirve para autopublicar contenido en una página de Facebook. Funciona de la siguiente manera: 
# 1. Crea una carpeta para cada día de la semana (monday, tuesday, wednesday, thursday, friday, satuday y sunday).
# 2. Dentro de cada carpeta se pueden crear archivos de texto (.txt) o imágenes (.jpg o .png).
# El script se encarga de publicar el contenido de cada archivo de texto en la página de Facebook.
# Si existe una imagen con el mismo nombre que el archivo de texto, se publica la imagen junto con el texto.
# Si no existe una imagen con el mismo nombre que el archivo de texto, se publica solo el texto.
# Si existe una imagen sin un archivo de texto con el mismo nombre, se publica solo la imagen.
# Si existe un archivo que no sea de texto ni imagen, se ignora y no se publica.
# 3. El script se ejecuta automáticamente cada día de la semana a las 8:00 am.


access_token = 'TOKEN'
app_id = 'APP_ID'
page_id = 'PAGE_ID'

def publicar_contenido_en_facebook(contenido, imagenes=None):
    url = f'https://graph.facebook.com/{page_id}/photos'
    params = {
        'access_token': access_token,
        'message': contenido,
    }

    if imagenes is not None:
        attached_media = []
        for imagen in imagenes:
            with open(imagen, 'rb') as file:
                file_content = file.read()
                attached_media.append(('source', (file.name, file_content, 'image/jpeg')))
        
        response = requests.post(url, params=params, files=attached_media)
    else:
        response = requests.post(url, params=params)

    if response.status_code == 200:
        print('Contenido publicado en Facebook correctamente.')
    else:
        print('Ha ocurrido un error al publicar en Facebook.')


def publicar_contenido_diario():
    print('Publicando contenido en Facebook...')
    directorio_publicaciones = 'publicaciones'

    dia_semana_actual = datetime.now().strftime('%A').lower()
    ruta_carpeta_dia_semana = os.path.join(directorio_publicaciones, dia_semana_actual)

    if os.path.exists(ruta_carpeta_dia_semana):
        archivos = os.listdir(ruta_carpeta_dia_semana)
        imagenes = []
        contenido = ''

        for archivo in archivos:
            ruta_archivo = os.path.join(ruta_carpeta_dia_semana, archivo)
            nombre_archivo, extension = os.path.splitext(archivo)

            if extension == '.txt':
                with open(ruta_archivo, 'r') as file:
                    contenido = file.read()

            elif extension in ('.jpg', '.png'):
                imagenes.append(ruta_archivo)

            else:
                print(f'Archivo no compatible: {ruta_archivo}')

        publicar_contenido_en_facebook(contenido, imagenes)

    else:
        print(f'No existe la carpeta para el día de la semana actual: {ruta_carpeta_dia_semana}')

schedule.every().day.at("08:00").do(publicar_contenido_diario)

while True:
    schedule.run_pending()
    time.sleep(60)
    print('Esperando a que sea la hora de publicar...') 
