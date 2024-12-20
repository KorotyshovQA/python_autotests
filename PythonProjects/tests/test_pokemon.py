import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'af222279d5c9f0b22cd78ff93e539fe6'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '12294'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name_in_response():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Герман'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Герман'),('id', TRAINER_ID),('city', 'Питер')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value