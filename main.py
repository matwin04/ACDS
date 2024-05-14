from bottle import request, route, run, static_file, template, redirect
from bottle_pymysql import pymysql
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

conn = pymysql.connect(host='localhost',
                       user='root',
                       database='ACDS',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor
                       )
@route('/')
def index():
    return template('./pages/index.html')
@route('/players')
def players():
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
    username = request.forms.get('username')
    password = request.forms.get('password')
    cursror = conn.cursor()
    cursror.execute("INSERT INTO players (username, password) VALUES (%s,%s)",(username,password))
    conn.commit()
    cursror.close()
    redirect('/players')

@route('/players/<username>')
def player_details(username):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    return template('./pages/players/player_details.html',username=result['username'])

if __name__ == '__main__':
    run(host=IPAddr, port=5159, reloader=True, debug=True)