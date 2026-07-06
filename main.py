import requests
import os
from dotenv import load_dotenv
from datetime import datetime

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

# Request for create a graphic
        # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        #print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}'

# Any day
    # today = datetime(year=any_year, month=any_month, day=any_day)

today = datetime.now()

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '100',
}

# Request for creat a pixel in graph
        # response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
        # print(response.text)