import argparse
import subprocess

def descargar_video(url, resolucion='720'):
    try:
        comando = f'youtube-dl -f "bestvideo[height<={resolucion}]+bestaudio/best[height<={resolucion}]" {url}'
        subprocess.call(comando, shell=True)
        print("Descarga completada.")
    except Exception as e:
        print("Error al descargar el video:", str(e))


# Configurar los argumentos de línea de comandos
parser = argparse.ArgumentParser(description='Herramienta para descargar videos de YouTube.')
parser.add_argument('url', type=str, help='URL del video de YouTube')
parser.add_argument('--resolucion', type=str, default='720', help='Resolución del video (por defecto: 720)')

# Obtener los argumentos ingresados por el usuario
args = parser.parse_args()

# Llamar a la función para descargar el video
descargar_video(args.url, args.resolucion)
