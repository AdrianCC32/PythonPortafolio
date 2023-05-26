import requests
from bs4 import BeautifulSoup
import os


def descargar_imagenes(url, carpeta_destino):
    try:

        response = requests.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, "html.parser")

            etiquetas_img = soup.find_all("img")

            for img in etiquetas_img:

                url_imagen = img["src"]

                if not url_imagen.startswith("http"):
                    url_imagen = url + url_imagen

                # Obtener el nombre de archivo de la URL
                nombre_archivo = url_imagen.split("/")[-1]

                # Verificar si la carpeta de destino existe, si no, crearla
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                response_img = requests.get(url_imagen)

                if response_img.status_code == 200:

                    ruta_archivo = os.path.join(
                        carpeta_destino, nombre_archivo)
                    with open(ruta_archivo, "wb") as archivo:
                        archivo.write(response_img.content)

                    print(
                        f"La imagen {nombre_archivo} se ha descargado correctamente.")
                else:
                    print(f"No se pudo descargar la imagen {nombre_archivo}.")

        else:
            print("No se pudo acceder a la página web.")

    except Exception as e:
        print(f"Ocurrió un error al descargar las imágenes: {str(e)}")


# URL de la página web
url_pagina = "https://www.google.com/"

# Carpeta de destino donde se guardarán las imágenes descargadas
carpeta_destino = "imagenes"

descargar_imagenes(url_pagina, carpeta_destino)
