import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bdce58a787784434ada2e64ec87a6c7e'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN}
TRAINER_ID = '43734'

def test_status_code_pokemons():
    response_pokemons = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_pokemons.status_code == 200

def test_status_code_trainers():
    response_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainers.status_code == 200

def test_part_of_response_pokemons():
    response_pokemons = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_pokemons.json()["data"][3]["name"] == 'Python'

def test_part_of_response_trainers():
    response_trainers = requests.get(url=f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_trainers.json()["data"][0]["trainer_name"] == 'Катерина'

@pytest.mark.parametrize('key, value', [('name', 'Python'),('trainer_id', TRAINER_ID),('id', '901018')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][3][key] == value
