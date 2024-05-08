from app import app
from flask import render_template
from flask import request

@app.route('/') #Configurando uma rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Diego")