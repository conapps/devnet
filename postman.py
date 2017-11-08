import requests

url = "https://api.ciscospark.com/v1/messages"

payload = "{\n\t\"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vZDBlNmRlYjAtYzQ5Mi0xMWU3LTgxOTMtODdiMGQ4YTU1YzU3\",\n\t\"text\": \"Mensaje desde Postman\"\n}"

headers = {
    'authorization': "Bearer Zjk2MmFiMTgtNGY2MS00Yzc2LTlmOWMtMzI2M2VmNjVkMTVlNWMyMzMyMzQtMGZj",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "65008c1a-f2e0-c3ea-568d-523179b3709c"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
