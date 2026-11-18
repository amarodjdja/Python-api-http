import requests


comuna_destino = 'Valparaíso'  # comuna asociada al envío
url = 'https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php'


respuesta = requests.get(url)

print(respuesta.status_code)
print(respuesta.text)