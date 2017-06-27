"""
Meraki API Test script
"""
import json
from meraki_api import MerakiAPI

KEY = "76268186c0b0da0eb10af1ba92419703930f9322"
SERIAL = "Q2JD-XK95-Y9D5"
ORGANIZATION_ID = "405942"
NETWORK_ID = "L_579838452023952619"

if __name__ == "__main__":

    def puts(text):
        """ Prints a text after JSON stringifying it """
        print(json.dumps(text, indent=2))
    
    '''
    # Crear un usuario de administrador en la organización ORGANIZATION_ID
    print("\nCreating a new organization user")
    ADMIN = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins()
        .create({
            "email": "g_monne@yahoo.com",
            "name": "Guzman Monne",
            "orgAccess": "none",
            "tags": [{
                "tag": "preventa",
                "access": "read-only"
            }]
        })
    )
    puts(ADMIN.json())
    # Elimina el administrador creado en la organización.
    print("Deleting user", ADMIN.json()["id"])
    RESPONSE = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins(ADMIN.json()["id"])
        .delete()
    )
    print('Admin created and deleted.')
    # Trae todos los cliente registrados en un determinado equipos en los
    # ultimos `timespan` milisegundos.
    print("\nGet clients connected to the device.", SERIAL)
    puts(
        MerakiAPI(KEY)
        .devices(SERIAL)
        .clients({"timespan": 86400})
        .json()
    )
    # Trae todas las redes dentro de una organization.
    print("\nGet all the networks inside organization", ORGANIZATION_ID)
    puts(
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .index()
        .json()
    )
    # Trae detalles de una network.
    print("\nGet the details of network", NETWORK_ID)
    puts(
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .show()
        .json()
    )
    print("\nUpdate network", NETWORK_ID)
    # Actualiza una network.
    puts(
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .update({
            "tags": "tag_desde_api"
        })
        .json()
    )
    # Crea una nueva network dentro de una organization.
    print("\nCreated a new network inside organization", ORGANIZATION_ID)
    JSON = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .create({
            "name": "Red creada por la API",
            "type": "wireless",
            "tags": "tag_desde_api otra_tag",
            "timeZone": "America/Montevideo"
        })
        .json()
    )
    puts(JSON)
    # Elimina una network.
    (
        MerakiAPI(KEY)
        .networks(JSON["id"])
        .delete()
    )
    print('Network created and deleted.')
    # Traer todos los clientes detectados en un dispositivo.
    print("\nAll detected clients on device", SERIAL)
    puts(
        MerakiAPI(KEY)
        .devices(SERIAL)
        .clients({"timespan": 86400})
        .json()
    )
    '''
    # Trae el tráfico de analisis en una red.
    print("\nGets the traffic analisis from the second network.")
    NETWORK_ID = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .index()
        .json()
    )[1]["id"]
    puts(
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .traffic({
            "timespan": 7200,
            "deviceType": "wireless"
        })
        .json()
    )
