# DNA Center

## Documentación de la API

[https://developer.cisco.com/site/dna-center-rest-api/](https://developer.cisco.com/site/dna-center-rest-api/)

## Introducción

El controlador DNA Center expone una API REST "Norte" que permite a los ingenieros y a las aplicaciones interactuar con el mismo de forma programática.

El controlador DNA Center también cuenta con interfaces "Sur" hacia el plano de control de la red; utiliza las mismas para gestionar e interactuar con los dispositivos de red.

De esta forma podemos utilizar la API Rest (Norte) para configurar el controlador y agregar funcionalidades de SDN a los equipos de red de forma dinámica.

## RBAC & service tokens

The Role-Based Access Control (RBAC) mechanism on the Cisco DNAC assigns a security role to every user account. That role determines which Cisco DNAC resources and operations are available for that user account.

The Cisco DNAC controller defines the following roles and privileges:

* **Administrator (SUPER_ADMIN-ROLE)** provides the user with full administrative privileges to all Cisco DNAC resources, including the ability to add or remove users and accounts.
* **Network Administrator (NETWORK_ADMIN-ROLE)** enables the user to provision, upgrade and change the configuration of network devices.
* **Observer (OBSERVER-ROLE)** provides the user with primarily read-only privileges to the Cisco DNAC.
* **Telemetry (TELEMETRY-ADMIN-ROLE)** enables the user to administer the telemetry (Assurance) configuration.

A security token known as a service token encapsulates user identity and role information as a single value.

RBAC-governed APIs use the service token to make access-control decisions. Therefore, to start, you send the Cisco DNAC a POST /token request with your username and password. If the DNAC controller authenticates your request, it returns a service token that encapsulates the role associated with the authenticated user account.

After you get the service token, you include it in all of the subsequent calls you send to the controller. When the controller receives those calls, it checks the service token before performing the action requested by the call.

## Generate a service token (script 14a)

To get a service token:

1.  Locate the 14a-DNAC-get-token.py.
2.  Use a Python command to run the script. For example:
    * On Linux or Mac OS: python3 14a-DNAC-get-token.py
    * On Windows: py -3 14a-DNAC-get-token.py or python 14a-DNAC-get-token.py
3.  Copy the service token printed in the console, navigate to [https://jwt.io](https://jwt.io), paste it inside "Encoded" text area and see the results in "Decoded" field.

> Observe that the function `HTTPBasicAuth` takes care of base64 encoding of the username and password and to include the encoded field in a header in the request.

**Bonus:**

> Read **Authentication/Authorization** section of the [API documentation](https://developer.cisco.com/site/dna-center-rest-api/), `import base64` and use the function `base64.b64encode(bytes(username + ':' + password, 'utf-8')).decode('utf-8')` to encode username:password in base64 and get the token **without** using `HTTPBasicAuth`.

## Prepare to reuse the generation of service tokens (script DNAC.py)

Now we are going to make a python module called `DNAC.py` with a function in it called `get_token(username, password)` that returns the service token as a string. Complete the script `DNAC.py` and obtain a re-usable function.

## Using the service token (Script 14c)

Almost every API call you send to Cisco DNAC REST must provide a service token; it doesn't matter whether the request is a POST, GET, PUT or DELETE. To provide the service token with your call, use an X-Auth-Token header. The header is a name-value pair that includes the value of your service token:

`{"X-Auth-Token": "service_token_value" }`

Replace service_token_value with the value of your service token. You don't have to get a new service token every time you make a request. However, the service token value must be valid and unexpired. In this lab, for simplicity, you start by getting a new service token each time you make a call to the API. Later, you'll see how to get and reuse a service token.

The following GET /host request shows how to use a service token. This request returns a list of DNAC hosts. The content of the list it returns is governed by the role of the caller. If the caller has an admin role, the response contains a list of all users. If the caller has an observer role, the response contains only the caller's user information.

The GET /host request does not require any arguments. Add an X-Auth-Token header to your GET /host request. The value of X-Auth-Token is the service token that your previous call to POST /token returned.

### Script 14c.

Start from the file `14c-DNAC-get-hosts.py` and modify it so it returns a list of hosts from DNAC.
