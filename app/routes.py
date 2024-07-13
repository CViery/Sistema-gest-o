from app import app
from flask import Flask, render_template, request, redirect, session
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
    

   

from flask import render_template, request, redirect, session
from app import app

@app.route('/cadastros/funcionarios')
def tela_cadastro_funcionario():
    if 'user' in session:
        return render_template('cadastrar_funcionario.html')
    else:
        return redirect('/')

@app.route('/cadastrar_funcionario', methods=['POST'])
def cadastrar_funcionario():
    if request.method == 'POST':
        # Aqui você deve processar os dados do formulário
        data = request.form.to_dict()
        # Exemplo de processamento dos dados (você precisa adaptar conforme sua lógica)
        # Após salvar, redirecione para a página de listagem de funcionários
        return redirect('/cadastros/funcionarios')


        

        

@app.route('/cadastros/clientes')
def tela_cadastro_fornecedor():
    if 'user' in session:
        return render_template('cadastrar_cliente.html')
    else:
        return redirect('/')

@app.route('/cadastrar_cliente', methods=['POST', 'GET'])
def cadastrar_forncedor():
    if request.method == 'POST':
         data = request.form.to_dict()
         
         return redirect('/cadastros/clientes')




