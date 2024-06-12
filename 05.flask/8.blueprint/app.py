import sys
import os
sys.path.append(os.path.abspath('admin'))
sys.path.append(os.path.abspath('product'))
from flask import Flask, render_template

from admin.admin import admin_app
from product.product import product_app

app = Flask(__name__)

# 각 블루프린트에 고유한 URL 접두사 부여
app.register_blueprint(admin_app, url_prefix="/admin")
app.register_blueprint(product_app, url_prefix="/products")

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
