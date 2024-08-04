import requests
import os
from dotenv import load_dotenv

# key 호출
load_dotenv()
print(os.environ)  # 모든 환경 변수 출력
print(f"YOUTUBE_API_KEY: {os.getenv('YOUTUBE_API_KEY')}")  # YouTube API 키만 출력

try:
    API_KEY = os.getenv('YOUTUBE_API_KEY')
    if API_KEY is None:
        raise ValueError("YOUTUBE_KEY not found in environment variables")

    url = 'https://www.googleapis.com/youtube/v3/search'

    search_query = 'Python programming'

    params = {
        'part': 'snippet',
        'q': search_query,
        'type': 'video',
        'maxResults': 10,
        'key': API_KEY
    }

    response = requests.get(url, params)
    response.raise_for_status()

    data = response.json()
    print("API 요청 성공!")
    print(f"검색 결과 수: {len(data.get('items', []))}")

    # 검색 결과 출력
    for item in data.get('items', []):
        print(f"제목: {item['snippet']['title']}")
        print(f"채널: {item['snippet']['channelTitle']}")
        print(f"설명: {item['snippet']['description'][:50]}...")  # 설명의 처음 50자만 출력
        print("---")

except requests.exceptions.RequestException as e:
    print(f"API 요청 중 오류 발생: {e}")
except KeyError as e:
    print(f"응답 데이터 처리 중 키 오류: {e}")
except ValueError as e:
    print(f"값 오류: {e}")
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")