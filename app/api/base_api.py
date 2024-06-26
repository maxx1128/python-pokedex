import requests


class BaseAPI:
  ROOT_URL = 'https://pokeapi.co/api/v2/'

  def test_request(self):
    response = requests.get(self.ROOT_URL + 'pokemon/ditto')
    data = response.json()
    print(data['abilities'])
