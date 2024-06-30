from app import app
from flask import render_template, redirect, session, request




@app.route('/')
def home():
        return render_template('index.html')

@app.route('/login')
def login():
    try:
        pass
    except Exception as e:
         print(e)
         
@app.route('/autenticar')
def autenticar():
    try:
        user = request.form['usuario']
        password = request.form['password']
        if user == 'admin'
    except Exception as e:
         print(e)