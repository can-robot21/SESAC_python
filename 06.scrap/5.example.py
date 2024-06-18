import requests
from bs4 import BeautifulSoup

url = 'https://www.pythonscraping.com/pages/page3.html'

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

table_tag = soup.select_one("#giftList")

product_trs = table_tag.select("tr")
# print(product_trs)
for product_tr in product_trs[1:]:
    product_tds = product_tr.select('td')
    print(f"상품명: {product_tds[0].text.strip()}, 가격: {product_tds[2].text.strip()}")