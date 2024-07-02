from app import app
from flask import render_template, redirect, session, request
from services import login



aut = login.Login()
@app.route('/home')
def home():
        if 'user' in session:
            return render_template('index.html')
        else:
             return redirect('/')

@app.route('/')
def tela_login():
    try:
        return render_template('login.html')
    except Exception as e:
         print(e)
         
@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar():
    try:
        user = request.form['username']
        password = request.form['password']
        login = aut.autenticar(user, password)
        if login:
            session['user'] = user
            return redirect('/home')
        else:
             return redirect('/')
    except Exception as e:
         print(e)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')
     
@app.route('/cadastros')
def tela_cadastros():
    if 'user' in session:
        return render_template('cadastros.html')
    else:
        return redirect('/')