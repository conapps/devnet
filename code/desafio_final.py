import requests
import sys

# Constante que contiene el umbral de tráfico en Bytes
UMBRAL = int(sys.argv[1])

# Constante que contiene el lapso de tiempo que hay que medir (un mes) medido en segundos
TIME_SPAN = 2592000

# Clave para poder autenticar con la API de Meraki
MERAKI_KEY = "a76b0e7d1d10b67bac8b4c87f54de4d09c9aa4fa"

# Nombre de la organización en Meraki que contiene la red para la cuál hay que obtener estadísticas
ORG_NAME = 'C001 - CONATEL S.A.'

# Nombre de la red para cuál hay que obtener estadísticas
NETWORK_NAME = 'W001 - Wireless ACME'

# Nombre de la sala donde hay que publicar las alarmas de tráfico
SPARK_ROOM_NAME = 'ACME IT Room'

