from flask import Flask, render_template, url_for, redirect, session
from datetime import timedelta

items = {
    'item1': {'name': '상품1', 'price': 1000},
    'item2': {'name': '상품2', 'price': 2000},
    'item3': {'name': '상품3', 'price': 3000}
}

app = Flask(__name__)
app.secret_key = 'sesac1234'
app.permanent_session_lifetime = timedelta(minutes = 5) # 5분 후 만료

@app.route('/')
def home():
    return render_template('index.html', items = items)

@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    print(f'상품담기: {item_name}')
    if 'cart' not in session:
        session['cart'] = {}
    session['cart'][item_name] = session['cart'].get(item_name, 0) + 1
    session.modified = True  # 세션 변경 사항 알림
    print(f"현재 장바구니: {session['cart']}")
    return redirect(url_for('home'))

@app.route('/remove_item_from_cart/<item_name>')
def remove_item_from_cart(item_name):
    print(f'상품 지우기: {item_name}')
    if 'cart' in session and item_name in session['cart']:
        session['cart'].pop(item_name, None)
        session.modified = True  # 세션 변경 사항 알림
    return redirect(url_for('view_cart'))

@app.route('/clear_cart')
def clear_cart():
    print(f'카트 비우기')   
    if 'cart' in session:
        session.pop('cart')
        session.modified = True         
    
    return redirect(url_for('view_cart'))

@app.route('/view_cart')
def view_cart():
    cart_items = {}
    total_price = 0
    
    for item_name, quantity in session.get('cart', {}).items():
        item_info = items.get(item_name)
        if item_info:
            cart_items[item_name] = {'name': item_info['name'], 'quantity': quantity, 'price': item_info['price']}
            total_price += item_info['price'] * quantity
        
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)


if __name__ == "__main__":
    app.run(debug=True)