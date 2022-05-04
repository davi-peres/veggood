import json


def busca_json(query):
    restaurante_db = open("restaurantes.txt","r")
    parsed_json = json.loads(restaurante_db.read())
    for i in parsed_json['restaurantes']:
        if str(query).lower() in str(i['nome']).lower():
            return i['url']
    return None