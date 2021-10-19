from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app= Flask(__name__, template_folder='template')
app.secret_key = 'dum56523'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "projeto"

mysql= MySQL(app)

@app.route('/')
def a():
    return redirect(url_for('login'))

@app.route('/login/', methods=['POST','GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'senha' in request.form:
        email = request.form['email']
        senha = request.form['senha']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM dados WHERE email = %s AND senha = %s', (email, senha,))
        conta = cursor.fetchone()
        if conta:
            session['loggedin'] = True
            session['id'] = conta['id']
            session['email'] = conta['email']
            return redirect(url_for('home'))
        else:
            msg = 'Email/senha Incorretos!'
    return render_template('login.html', msg=msg)


@app.route('/login/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('email', None)
   return redirect(url_for('login'))

@app.route('/login/cadastro', methods=['GET','POST'])
def cadastro():
    msg=''
    if request.method=='POST':
        nome= request.form['nome']
        cpf= request.form['cpf']
        pis= request.form['pis']
        pais= request.form['pais']
        estado= request.form['estado']
        municipio= request.form['municipio']
        cep= request.form['cep']
        logradouro= request.form['logradouro']
        numero=request.form['numero']
        complemento= request.form['complemento']
        email= request.form['email']
        senha= request.form['senha']
        cursor= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM dados WHERE email = %s', (email,))
        conta = cursor.fetchone()
        if conta:
            msg = 'Conta ja existente!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Email invalido'
        elif not nome or not cpf or not pis or not pais or not estado or not municipio or not cep or not logradouro or not numero or not complemento or not email or not senha:
            msg = 'Por favor, preencha o formulário!'
        else:
            cursor.execute("INSERT INTO dados (nome,cpf,pis,pais,estado,municipio,cep,logradouro,numero,complemento,email,senha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(nome,cpf,pis,pais,estado,municipio,cep,logradouro,numero,complemento,email,senha))
            mysql.connection.commit()
            cursor.close()    
            msg = 'sucesso'   
            return redirect(url_for('login'))
    elif request.method == 'POST':
        msg = 'Por favor, preencha o formulário!'
    return render_template('cadastro.html', msg=msg)
    

@app.route('/login/home')
def home():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT nome FROM dados WHERE id = %s', (session['id'],))
        conta = cursor.fetchone()
        return render_template('home.html', conta=conta)
    return redirect(url_for('login'))

@app.route('/login/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM dados WHERE id = %s', (session['id'],))
        conta = cursor.fetchone()
        return render_template('profile.html', conta=conta)
    return redirect(url_for('login'))


@app.route('/login/alteracao/', methods=['GET','POST'])
def alteracao():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM dados WHERE id = %s', (session['id'],))
        conta = cursor.fetchone()
        return render_template('alteracao.html', conta=conta)

@app.route('/login/update/', methods=['GET','POST'])
def update():
    if request.method =='POST':
        nome= request.form['nome']
        cpf= request.form['cpf']
        pis= request.form['pis']
        pais= request.form['pais']
        estado= request.form['estado']
        municipio= request.form['municipio']
        cep= request.form['cep']
        logradouro= request.form['logradouro']
        numero=request.form['numero']
        complemento= request.form['complemento']
        email= request.form['email']
        senha= request.form['senha']
        cursor= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("UPDATE dados SET nome=%s, cpf=%s, pis=%s, pais=%s, estado=%s, municipio=%s, cep=%s, logradouro=%s, numero=%s, complemento=%s, email=%s, senha=%s WHERE id=%s",(nome,cpf,pis,pais,estado,municipio,cep,logradouro,numero,complemento,email,senha,session['id']))
        mysql.connection.commit()
        cursor.close()       
        return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(debug=True) 


