from flask import Flask, render_template, request
import folium
from folium.plugins import MarkerCluster
import random

app = Flask(__name__)

def generate_random_coordinate(num):
    # 랜덤으로 GPS 좌표 만들기
    coordinates = []
    
    for _ in range(num):
        lat = random.uniform(37.4, 37.7)  # 서울시의 위도 범위
        lng = random.uniform(126.8, 127.1)
        coordinates.append([lat, lng])
        
    return coordinates

def create_map(num_points):
    seoul_center = [37.5665, 126.9700]
    map = folium.Map(location=seoul_center, zoom_start=12)
    
    # 좌표 만들기
    coordinates = generate_random_coordinate(num_points)
    
    marker_cluster = MarkerCluster().add_to(map)
    for coord in coordinates:
        folium.Marker(location=coord).add_to(marker_cluster)
    
    return map

@app.route('/')
def index():
    return render_template('index_random.html')

@app.route('/map', methods=['GET'])
def map_points():
    num_points = int(request.args.get('num_points', 10))  # 기본값을 10으로 설정
    mymap = create_map(num_points)
    map_html = mymap._repr_html_()
    
    return render_template('index_random.html', map_html=map_html)

if __name__ == "__main__":
    app.run(debug=True)
