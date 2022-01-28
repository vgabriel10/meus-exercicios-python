"""
 Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import requests

try:
    url = "http://pudim.com.br"
    pagina = requests.get(url)
    estado = pagina.status_code
    if (estado == 200):
        print('Site Ativo')
except:
    print('O site não acessivel no momento!')


