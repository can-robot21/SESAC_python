import requests  
from dotenv import load_dotenv  
import os

load_dotenv()  

API_KEY = os.getenv('KAKAO_API_KEY')

query = '뉴진스'

url = "https://dapi.kakao.com/v2/search/image"
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

print(f"검색어 '{query}'에 대한 이미지 검색 결과:")
print(f"총 {len(data['documents'])}개의 결과를 찾았습니다.\n")

for i, item in enumerate(data["documents"], 1):
    print(f"이미지 {i}:")
    print(f"썸네일 URL: {item['thumbnail_url']}")
    print(f"원본 이미지 URL: {item['image_url']}")
    print(f"너비: {item['width']}px")
    print(f"높이: {item['height']}px")
    print(f"문서 URL: {item['doc_url']}")
    print(f"출처: {item['display_sitename']}")
    print("---")

# 메타데이터 출력
if 'meta' in data:
    print("\n메타 정보:")
    print(f"총 검색 가능 문서 수: {data['meta']['total_count']}")
    print(f"현재 페이지 번호: {data['meta']['pageable_count']}")
    print(f"마지막 페이지 여부: {'예' if data['meta']['is_end'] else '아니오'}")