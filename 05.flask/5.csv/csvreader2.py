import csv
import math
from flask import Flask, render_template

app = Flask(__name__)

csv_data = []

def load_csv_data(filename):
    global csv_data
    with open(filename, newline='', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            csv_data.append(row)

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    per_page = 20
    # print("출력: ", csv_data)
    headers = csv_data[0]
    
    start_index = (page - 1) * per_page + 1
    end_index = start_index + per_page
    
    total_pages = (len(csv_data) + per_page -1) // per_page
    return render_template("index2.html", headers=headers, users=csv_data[start_index:end_index], total_pages= total_pages)

if __name__ == '__main__':
    load_csv_data('./user.csv')
    # print(csv_data)
    app.run(debug=True)