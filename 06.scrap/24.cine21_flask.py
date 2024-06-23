from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_conntion():
    conn = sqlite3.connect('movie.db')
    conn.row_factory = sqlite.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM movies')
    rows = cur.fetchall()
    conn.close()
    
    movie = []
    for row in rows:
        movie.append(
            {'rank': row['rank'],
            'title': row['title'],
            'audience': row['audience']}
        )
        
    return render_templaste('movie.html', movie=movie)

if __name__ == "__main__":
    app.run(debug=True)