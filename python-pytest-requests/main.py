import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bdce58a787784434ada2e64ec87a6c7e'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN}

body_create = {
    "name": "Питон",
    "photo_id": 24
}

body_changeName = {
    "pokemon_id": "901018",
    "name": "Python",
    "photo_id": 23
}

body_pokeball = {
    "pokemon_id": "901024"
}

'''response_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''


'''response_changeName = requests.put(url=f'{URL}/pokemons', headers= HEADER, json=body_changeName)
print(response_changeName.text)'''

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)
