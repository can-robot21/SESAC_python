import random
import uuid
import json 
from print import printData
from generator_id import generate_uuid

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

def generate_i():   
    for category, items_info in json_data.items():
        for item_name, item_price in items_info.items():
            item_id = generate_uuid()
            items.append((item_id, item_name, category, item_price))
    print("메뉴 정리: ", items)
    return items
            
if __name__  == "__main__":
    generate_items = input("아이템 생성하시겠습니까?:(YES or No) ")
    if generate_items.upper() == "YES":
        data = generate_i()
        num_items = len(data)
        printData("i", num_items)