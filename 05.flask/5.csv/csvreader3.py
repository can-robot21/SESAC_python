import csv
import math
from flask import Flask, render_template

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
    # print("출력: ", csv_data)
    print(f" 해더: {headers}")
    
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    
    total_pages = math.ceil(len(csv_data) / per_page)
    return render_template("user2.html", headers=headers, users=csv_data[start_index:end_index], total_pages= total_pages)

if __name__ == '__main__':
    load_csv_data('./user.csv')
    # print(csv_data)
    app.run(debug=True)