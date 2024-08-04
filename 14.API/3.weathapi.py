import requests
from dotenv import load_dotenv
import os

# dotenv 호출
load_dotenv()

OWM_API_KEY = os.getenv('OPENWEATHERMAP_KEY')

url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'q': 'Seoul', 
    'appid': '2cfe0c87e181a1eb0cca25c6680d7b99',
    'units': 'metric',
    'lang':'kr' # 결과 언어
}

response = requests.get(url, params=params)
response = requests.raise