from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>간단한 HTML</title>
</head>
<body>
    <h1>안녕하세요</h1>
    <p>이것은 간단한 HTML 예제입니다. </p>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')
# print(html_doc)
# print(soup)
