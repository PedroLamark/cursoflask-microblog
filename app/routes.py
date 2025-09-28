from app import app
from flask import render_template, redirect, request, flash


@app.route('/', defaults={'nome':'User', 'profissao': 'Dev', 'empresa': 'LamarksCorp'})
@app.route('/index', defaults={'nome':'User', 'profissao': 'Dev', 'empresa': 'LamarksCorp'})
@app.route('/index/<nome>/<profissao>/<empresa>')

def index(nome, profissao, empresa):
    dados = {'Profissao': profissao, 'Empresa': empresa}

    return render_template(
        'index.html', 
        nome=nome, 
        dados=dados
    )

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST'])
def autenticar():
    user = request.form.get('user')
    passwd = request.form.get('pass')

    if(user == 'admin' and passwd == '1234'):
        return f'usuario {user} & senha {passwd}'
    else:
        flash('Dados inválidos')
        return redirect('/login')

