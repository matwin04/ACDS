from bottle import request, route, run, static_file, template, redirect
import socket
import os.path
import sqlite3

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
DATABASE = 'acds.db'
SQL_SCRIPT = 'createdb.sql'
def connectDB():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn
def initDB():
    with sqlite3.connect(DATABASE) as conn:
        with open(SQL_SCRIPT,'r') as f:
            conn.executescript(f.read())
    if not os.path.exists(DATABASE):
        print("DB INITIALIZED")
    else:
        print("DB ALLREADY EXISTS")
@route('/')
def index():
    return template('./pages/index.html')
@route('/players')
def index():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return template('./pages/players/players.html',rows=result)
@route('/records')
def laps():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM laps")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return template('./pages/laps/laps.html', rows=result)

@route('/add_player')
def add_player_form():
    return static_file('/players/newplayer.html', root='./pages')
@route('/add_player',method='POST')
def add_player():
    name = request.forms.get('name')
    username = request.forms.get('username')
    email = request.forms.get('email')
    conn = connectDB()
    cursror = conn.cursor()
    cursror.execute("INSERT INTO players (name, username, email) VALUES (?,?,?)",(name,username,email))
    conn.commit()
    cursror.close()
    conn.close()
    redirect('/players')

@route('/players/<username>')
def player_details(username):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE username = ?", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return template('./pages/players/player_details.html', username=result['username'])

if __name__ == '__main__':
    initDB()
    run(host=IPAddr, port=5159, reloader=True, debug=True)