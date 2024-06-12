from flask import Blueprint

product_app = Blueprint('product', __name__)

@product_app.route("/")
def product_home():
    return "<h1>제품 페이지</h1>"
