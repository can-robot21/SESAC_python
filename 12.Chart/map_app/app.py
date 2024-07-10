from flask import Flask, render_template
import folium
from folium.plugins import MarkerCluster

app = Flask(__name__)

@app.route('/')
def index():
    # 커피샵 데이터 
    coffee_shops = {
        'chungdaum': [
            {'name': '커피샵 1호', 'latitude': 37.5667, 'longitude': 126.9700},
            {'name': '커피샵 2호', 'latitude': 32.5667, 'longitude': 126.9700},
            {'name': '커피샵 3호', 'latitude': 31.5667, 'longitude': 116.9700}            
        ],
        'jamsil': [
            {'name': '커피샵 1호', 'latitude': 37.5667, 'longitude': 126.9700},
            {'name': '커피샵 2호', 'latitude': 32.5667, 'longitude': 126.9700},
            {'name': '커피샵 3호', 'latitude': 31.5667, 'longitude': 116.9700}            
        ],
        'junggu': [
            {'name': '커피샵 1호', 'latitude': 37.5667, 'longitude': 126.9700},
            {'name': '커피샵 2호', 'latitude': 32.5667, 'longitude': 126.9700},
            {'name': '커피샵 3호', 'latitude': 31.5667, 'longitude': 116.9700}            
        ]
    }
    
    # 서울 중심으로 세팅
    map_center = [37.5665, 126.9700]
    
    mymap = folium.Map(location=map_center, zoom_start=12)
    
    # 클러스터 추가
    marker_cluster = MarkerCluster().add_to(mymap)
    for area, shops in coffee_shops.items():
        for shop in shops:
            folium.Marker(
                location=[shop['latitude'], shop['longitude']],
                popup=shop['name']
            ).add_to(marker_cluster)
    
    # html 저장
    map_html = mymap._repr_html_()
    
    return render_template('index_map.html', map_html=map_html)

if __name__ == "__main__":
    app.run(debug=True)
