import requests
import json

cep = input("Digite seu cep")

req = requests.get("https://viacep.com.br/ws/"+cep+"/json")


if req.status_code == 200:
    print("Requisição realizada com sucesso.")
    response = json.loads(req.content)
    print(response)
else:
    print("Ocorreu um erro na requisição")