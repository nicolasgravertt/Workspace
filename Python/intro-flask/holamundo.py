# Post cuando quieres crear
# Get cuando quieres listar
# Put cuando quieres actualizar
# delete cuando quieres eliminar
# patch cuando quieres actualizar parcialmente.
from flask import Flask, request , url_for, redirect, abort
from flask.templating import render_template
app = Flask(__name__)

import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hola123.",
    database="prueba"
)

cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/post/<post_id>', methods=['GET','POST'])
def lala(post_id):
    return 'El id del post es: ' + post_id

@app.route('/lele',methods=['POST','GET'])
def lele():

    cursor.execute('select * from usuario')
    usuarios = cursor.fetchall()

    #abort(401)
    #return redirect(url_for('lala', post_id=2))
    #print(request.form)
    #print(request.form['llave1'])
    #print(request.form['llave2'])
    #return 'lele.html'
    #return render_template('lele.html')
    #return{
    #    "username": 'hola',
    #    "email": 'hola@hola.com'
    #}
    return render_template('lele.html',usuarios=usuarios)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Mundo')

@app.route('/crear',methods=['POST','GET'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        sql = 'insert into usuario (username,email) values(%s,%s)'
        values = (username,email)
        cursor.execute(sql,values)
        midb.commit()

        return redirect(url_for('lele'))
    return render_template('crear.html')
    