import random

cities = ['서울시 동대문구', '서울시 서대문구', '서울시 종로구', '서울시 중구', '서울시 광진구', '경기도 성남시', '경기도 부천시', '경기도 남양주시', '경기도 구리시', '인천시 남동구', '인천시 서구', '인천시 부평구', '인천시 남동구']
streets = ['느티로 2', '금강로 333', '산마루로 24', '중앙로 245', '세종로 14', '통이로 135', '경기대로 13', '충정로 11길', '신촌로 223', '왕산로 239', '제기로 117', '천호대로 21']

def generate_address():
    address = cities[random.randint(0, len(cities)-1)]+" "+streets[random.randint(0,len(streets)-1)]
    
    return address