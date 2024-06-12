from flask import Blueprint

admin_app = Blueprint('admin', __name__)

@admin_app.route("/") 
def admin_home():
    return "<h1>관리자 페이지</h1>"
