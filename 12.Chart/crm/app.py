from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    # SQL을 통해서.. DB에서 가져오는것만 구현하면 끝~~~
    
    data = { # 아래 파이썬의 dict 형태임..
        'labels' : ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06'],
        'revenue' : [797500, 401500, 665500, 660000, 566500, 709500]
    }
    return jsonify(data) # 내가 가지고 있는 dict 데이터를... JSON으로 변환해서 전달해라..

if __name__ == "__main__":
    app.run(debug=True)
