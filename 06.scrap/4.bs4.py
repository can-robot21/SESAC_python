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
        <p>Copyright C 2024. <b>이 페이지는</b> <i>내꺼</i></p>
    </div>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser') # html.parser.xml

link_tag = soup.select_one('a')
print(link_tag)

all_imgs = soup.select_one('img')
print(all_imgs)

all_imgs = soup.select('img')
print(all_imgs)

content_div = soup.select_one('div.content') # div 하나만 선택 class 명
print(content_div)

footer_div = soup.select_one('div#footer') # div 하나만 선택 id 명
print(footer_div)

li_lists = soup.select('div.content li')
print('li_lists')

p_tag_div_footer = soup.select_one('div#footer p')
b_text = p_tag_div_footer.select_one('b').get_text()
t_text = p_tag_div_footer.select_one('i').get_text()

print(f'볼드: {b_text}, 텍스트: {t_text}')