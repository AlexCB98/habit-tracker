import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")

pixela_endpoint = 'https://pixe.la/v1/users'

user_parameters = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(
    url=pixela_endpoint,
    json=user_parameters,
)

print(response.text)