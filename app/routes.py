from app import app
from flask import render_template, redirect, session, request
from services import login, cadastros
import requests
from requests.structures import CaseInsensitiveDict


aut = login.Login()
cadastrar = cadastros.Cadastros()
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
    
@app.route('/cadastros/produtos')
def tela_cadastro_produtos():
    if 'user' in session:
        return render_template('cadastrar_produtos.html')
    else:
        return redirect('/')
    
@app.route('/cadastrar_produto', methods=['POST', 'GET'])
def cadastrar_produto():
    if request.method == 'POST':
         
         data = request.form.to_dict()
         cadastrar.cadastrar_peca(data)
         return redirect('/cadastros/produtos')

@app.route('/cadastros/fornecedores')
def tela_cadastro_fornecedor():
    if 'user' in session:
        return render_template('cadastrar_fornecedor.html')
    else:
        return redirect('/')

@app.route('/cadastrar_fornecedor', methods=['POST', 'GET'])
def cadastrar_forncedor():
    if request.method == 'POST':
         data = request.form.to_dict()
         
         return redirect('/cadastros/fornecedores')




