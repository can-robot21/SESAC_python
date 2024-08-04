from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('KAKAO_API_KEY')

def call_kakao_api(api_url, params):
    headers = {
        "Authorization": f"KakaoAK {API_KEY}"
    }
    
    response = requests.get(api_url, headers=headers, params=params)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    search_type = request.args.get('type', 'web')  # 기본값은 'web'
    
    if search_type == 'web':
        api_url = "https://dapi.kakao.com/v2/search/web"
    elif search_type == 'image':
        api_url = "https://dapi.kakao.com/v2/search/image"
    else:
        return "Invalid search type"
    
    params = {
        'query': query,
        'sort': 'accuracy',
        'page': 1,
        'size': 10
    }
    
    result = call_kakao_api(api_url, params)
    
    return render_template('result.html', result=result, query=query, search_type=search_type)

if __name__ == "__main__":
    app.run(debug=True)