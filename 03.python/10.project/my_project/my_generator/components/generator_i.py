import random
import uuid
import json 
from print import printData
from generator_id import generate_id

# 매장 아이템 juice, coffee, cake 
# 가격
json_data = {
    "COFFEE": 
        { '아메리카노': 2500, '카페라떼': 3000, '에스프레소': 3200 , '카푸치노': 3500, '모카라떼': 4000 },
    "JUICE": 
        { '오렌지주스':2800, '애플주스': 3200, '포도주스': 3600, '파인애플주스': 4200, '멜론주스': 4300 },
    "CAKE": 
        { '초코 스무디': 3500, '딸기 스무디': 3800, '바닐라 스무디': 4000, '수박 스무디': 4200, '요거트 스무디': 4500 },
    "BLEND": 
        { '바닐라 쉐이크': 3800, '초코 쉐이크': 4200, '그린티 쉐이크': 4200, '요거트 쉐이크': 4500, '딸기 쉐이크': 4800 }
}
items = []
item = ()

def generate_i(num):   
    for category, items_list in json_data.items():
        for item_name, item_price in items_list.json_items():
    
    item_id = (generate_id(), )
            
if __name__  == "__main__":
    num_items = int(input("생성 아이템 수를 입력하세요.: "))
    data = generate_i(num_items)
    
    printData("i", num_items)
