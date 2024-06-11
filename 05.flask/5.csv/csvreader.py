import csv
from flask import Flask, render_template

app = Flask(__name__)

csv_data = []

def load_csv_data(filename):
    csv_data  
    with open(filename, newline='', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            csv_data.append(row)

@app.route("/")
def index():
    print("출력: ", csv_data)
    return render_template("index.html", users=csv_data)

if __name__ == '__main__':
    load_csv_data('./data.csv')
    # print(csv_data)
    app.run(debug=True)