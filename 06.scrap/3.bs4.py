from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>간단한 HTML</title>
</head>
<body>
    <div class="container">
        <h1>안녕하세요</h1>
        <p>이것은 간단한 HTML 예제입니다. </p>
    </div>
    <a href="https://www.naver.com">네이버 링크</a>
    <img src="example1.jpg" alt="예제1">
    <img src="example2.jpg" alt="예제2">
    
    <div class="content">
        <ul>
            <li>항목 1</li>
            <li>항목 2</li>
            <li>항목 3</li>
        </ul>
    </div>
    <div id="footer">
        <p>Copyright C 2024. 이 페이지는 내꺼</p>
    </div>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')
# print(html_doc)
# print(soup)
# print(soup.head)

# list_items = soup.ul.find_all('li')
# print(list_items)

# container_div = soup.find('div', class_='container')
# print(container_div.h1.text)
# print(container_div.p.text)

# == 수정 필요 ==
# footer_div = soup.find('div', class_='footer')
# print(footer_div.p.text)

# ============ li 리스트 출력 ======================
# content_ul = soup.find('div', class_='content').ul
# # priint(content)

# for li in content_ul.find_all('li'):
#     print(li.text)

# link_tag = soup.a  # 가장 먼저 잡히는
# print(link_tag.text)
# naver_link = link_tag['href']
# print(naver_link)

# === 수정중
# import requests
# response = requests.get(naver_link)
# print(requests.text)

img_tag = soup.img 
print(img_tag['src'])
print(img_tag['alt'])

img_tags = soup.find_all('img')
img_tag1 = img_tags[0]
img_tag2 = img_tags[1]
print(f'이미지 테그1: ', img_tag1)
print(f'이미지 테그2: ', img_tag2)

print(f'소스: {img_tag.get("src")}, ALT글자: {img_tag.get("alt")}, width: {img_tag.get("width", "없음")}')
print(f'소스: {img_tag("src")}, ALT글자: {img_tag("alt")}, width: {img_tag("width", "없음")}')
