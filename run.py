#!bin/python
from flask import Flask, render_template, url_for, request,redirect,make_response,session
import os, sys, string
import MySQLdb

app = Flask(__name__)
# from app import views

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname':'miguel' } ##  users
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]

    try:
        conn = MySQLdb.connect(host='localhost',user='vpush',passwd='123',db='veffectsys')
    except Exception, e:
        print e
        sys.exit()
    cursor = conn.cursor()
    sql = "create table if not exists test1(name varchar(128) primary key, age int(4))"
    cursor.execute(sql)
    sql = "insert into test1(name, age) values ('%s', %d)" % ("zhaowei2", 23)
    try:
        cursor.execute(sql)
	print 'insert sql data'
    except Exception, e:
        print e
    print 'close cursor and conn!!'
    conn.commit()
    cursor.close()
    conn.close()
    if 'username' in session:
        return render_template("index.html", title = 'home xx ', user = user, posts= posts, username = username)
    
    return render_template("index.html", title = 'home xx ', user = user, posts= posts)






@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print '[ddebug] in request.method'
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html", title = 'Login html titile ')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0',debug=True)

