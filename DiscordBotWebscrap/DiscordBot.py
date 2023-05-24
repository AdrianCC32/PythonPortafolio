"""
Este script fue diseñado para un juego ONLINE, hace webscrap a la pagina de "highscores", el cual muestra una tabla con nombre/exp/nivel
este script lo que hace es buscar la exp que tiene cierto player "nombre", y si este supera un umbral de exp, el bot avisa en el canal de discord
"""

import discord
import asyncio
import requests
from bs4 import BeautifulSoup
from discord.ext import commands


intents = discord.Intents.default()  # Create a default Intents object
intents.typing = False  # Disable typing events (optional)

client = discord.Client(intents=intents)  # Pass the intents argument}

bot = commands.Bot(command_prefix='.', intents=intents)
enemy = []
print("Webscraping")
url = "https://www.example.net/highscores&list=experience"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


def check_number():
    print("Inicio")
    tr_elements = soup.find_all(
        'tr', attrs={'background': ['images/tablebg3.png', 'images/tablebg2.png']})
    for tr in tr_elements:
        td_elements = tr.find_all('td')
        # Verifica si hay al menos 4 elementos <td>
        cuarto_td = td_elements[3]
        segundo_td = td_elements[1]
        nombre = segundo_td.get_text()
        exp = cuarto_td.get_text()
        print(nombre + exp)
        numero_deseado = "17508441545"
        if "nombre Boost" in str(nombre):
            print("nombre encontrado")
            if int(exp) > int(numero_deseado):
                channel.send(nombre + "ha ganado experiencia!")
            else:
                return False


@client.event
async def on_ready():
    print(f'Bot conectado como {client.user.name}')
    await client.change_presence(activity=discord.Game(name='Verificando EXP'))
    while True:
        print("Inicio")
        tr_elements = soup.find_all(
            'tr', attrs={'background': ['images/tablebg3.png', 'images/tablebg2.png']})
        for tr in tr_elements:
            td_elements = tr.find_all('td')
            # Verifica si hay al menos 4 elementos <td>
            cuarto_td = td_elements[3]
            segundo_td = td_elements[1]
            nombre = segundo_td.get_text()
            exp = cuarto_td.get_text()
            print(nombre + exp)
            numero_deseado = "17508441545"
            if "Nombre" in str(nombre):
                print("Nombre encontrado")
                if int(exp) > int(numero_deseado):
                    server = client.get_guild(DISCORD_sERVER_ID)
                    channel = server.get_channel(DISCORD_CHANNEL_ID)
                    await channel.send(nombre + "ha ganado experiencia!")
                else:
                    return False
        await asyncio.sleep(60)  # Espera 1min antes de verificar nuevamente

client.run(
    'BOTTOKEN')
