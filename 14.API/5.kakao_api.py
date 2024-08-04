import requests  
from dotenv import load_dotenv  
import os

load_dotenv()  

API_KEY = os.getenv('KAKAO_API_KEY')

query = '이효리'

url = "https://dapi.kakao.com/v2/search/web"
headers = {
    "Authorization": f"KakaoAK {API_KEY}"  
}
params = {
    'query': query,
    'sort': 'accuracy',  # 정확도순
    'page': 1,
    'size': 10
}

response = requests.get(url, headers=headers, params=params) 
response.raise_for_status()
data = response.json()
print(data)
# for item in data["documents"]: