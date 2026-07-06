import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_USERNAME = os.getenv('PIXELA_USERNAME')
PIXELA_TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = os.getenv('GRAPH_ID')

pixela_endpoint = 'https://pixe.la/v1/users'

user_parameters = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# Request for create an account
      # response = requests.post(url=pixela_endpoint, json=user_parameters)
      # print(response.text)

graph_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Pushups',
    'unit': 'commit',
    'type': 'int',
    'color': 'sora',
}

headers = {
    'X-USER-TOKEN': PIXELA_TOKEN,
}

response = requests.post(
    url=graph_endpoint,
    json=graph_config,
    headers=headers,
)

print(response.text)