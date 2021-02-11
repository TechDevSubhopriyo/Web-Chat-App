from flask import *
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'abcd'

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_DB'] = 'chatapp'


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/chats')
def chats():
    mob = (request.args.get('mobile'))
    chatperson = (request.args.get('cperson'))
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM chats WHERE sender = '"+mob+"' OR receiver = '"+mob+"'"
    cursor.execute(sql)

    data = cursor.fetchall()
    unique = list()
    unique.clear()
    # for i in range(len(data)):
    #     if data[i][1] != mob and data[i][1] not in unique:
    #         unique.append(data[i][1])
    #     if data[i][2] != mob and data[i][2] not in unique:
    #         unique.append(data[i][2])
    for i in range(len(data)):
        if data[i][1] != mob:
            unique.append(data[i][1])
        if data[i][2] != mob:
            unique.append(data[i][2])
    unique.reverse()
    unique=list(dict.fromkeys(unique))
        
    return render_template('chats.html',persons = unique, user = mob, chats = data, cperson = chatperson)

@app.route('/register')
def register():
    mob = request.args.get('mobile')
    pin = request.args.get('pin')
    cursor = mysql.connection.cursor()
    check = "SELECT * FROM user WHERE mobile = '"+mob+"'"
    cursor.execute(check)

    data = cursor.fetchall()
    if len(data)>0:
        flash('Already Registered')
    else:
        sql = "INSERT INTO user (id, mobile, pin) VALUES (NULL,'"+mob+"','"+pin+"');"
        cursor.execute(sql)
        flash('Registered Successfully')
    return redirect('/',302, None)

@app.route('/login')
def login():
    mob = request.args.get('mobile')
    pin = request.args.get('pin')
    cursor = mysql.connection.cursor()
    check = "SELECT * FROM user WHERE mobile = '"+mob+"' AND pin = '"+pin+"'"
    cursor.execute(check)

    data = cursor.fetchall()
    if len(data)==1:
        return redirect('/chats?mobile='+mob,302, None)
    else:
        flash('Wrong Credentials')
        return redirect('/',302, None)

@app.route('/send')
def sendmessage():
    sender = request.args.get('sender')
    receiver = request.args.get('receiver')
    message = request.args.get('message')
    cursor = mysql.connection.cursor()
    sql = "INSERT INTO chats (sender, receiver, message) VALUES ('"+sender+"','"+receiver+"','"+message+"');"
    if receiver!='None':
        cursor.execute(sql)
        return redirect('/chats?mobile='+sender+'&cperson='+receiver,302, None)
    else:
        return redirect('/chats?mobile='+sender,302, None)

mysql = MySQL(app)
if __name__ == '__main__':
    app.run()