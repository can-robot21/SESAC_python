import csv, math
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

csv_data = []
headers = []

def load_csv_data(filename):
    global headers #글로벌 변수 : 바깥 변수를 내부에서 수정할 경우 선언함
    with open(filename, newline='', encoding='utf8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        headers = csv_reader.fieldnames
        for row in csv_reader:
            clean_row = {fieldname.strip(): value.strip() for fieldname, value in row.items()}
            csv_data.append(clean_row)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    per_page = 20
    name_query = request.args.get("name", "").lower().strip()
    
    if name_query:
        filtered_data = [item for item in csv_data if item['name'].lower() == name_query]
    else:
        filtered_data = csv_data
    
    
    total_pages = math.ceil(len(filtered_data) / per_page)
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    users = filtered_data[start_index:end_index]
    print(f" 데이터 내용: {users}")
    # 필터링된 데이터를 기반으로 템플릿 렌더링
    return render_template("index3.html", headers=headers, users=users, total_pages=total_pages)

        
    

if __name__ == '__main__':
    load_csv_data('./user.csv')
    # print(csv_data)
    app.run(debug=True)