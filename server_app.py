from bottle import request, route, run, static_file, template, redirect
from bottle_pymysql import pymysql
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


def connectDB():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           database='ACDS',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor
                           )
    return conn

@route('/')
def index():
    return template('./pages/index.html')
@route('/players')
def players():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    result = cursor.fetchall()
    cursor.close()
    return template('./pages/players/players.html',rows=result)
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
    cursror.execute("INSERT INTO players (username, password) VALUES (%s,%s)",(username,password))
    conn.commit()
    cursror.close()
    redirect('/players')

@route('/players/<username>')
def player_details(username):
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    return template('./pages/players/player_details.html',username=result['username'])
@route('/records')
def laps():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM laps")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return template('./pages/laps/laps.html',rows=result)
#CONTENT
@route('/content')
def index():
    return template('./pages/content/index.html')
@route('/content/cars')
def content():
    conn = connectDB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return template('./pages/content/cars.html',rows=result)
if __name__ == '__main__':
    connectDB()
    run(host=IPAddr, port=5159, reloader=True, debug=True)