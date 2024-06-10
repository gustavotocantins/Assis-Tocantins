from flask import Flask, render_template, url_for, request, redirect
from pickle import load
from re import match
from glob import glob
from os import chdir
import os
import json

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def sobre():
    return render_template('projetos.html')

@app.route('/whatsapp')
def whatsapp():
    return render_template('whatsapp.html')

@app.route('/GolSolidario')
def golsolidario():
    return render_template('GolSolidario.html')

@app.route('/ZAP')
def ZAP():
    return render_template('whatsapp.html')

@app.route('/participar')
def participar():
    return render_template('participar.html')

@app.route('/transicao')
def transicao():
    return render_template('transicao.html')

@app.route('/blog/pre-candidato-a-vereador-castanhal-2024')
def blog_post_pre_candidato():
    return render_template('blog-post-pré-candidato.html')

@app.route('/blog/vagas-de-emprego-whatsapp-castanhal')
def vagasdeemprego():
    return render_template('blog-grupodeemprego.html')

@app.route('/blog/grupo-whatsapp-castanhal')
def gruposzap():
    return render_template('blog-grupowhatsapp.html')


@app.route('/blog/castanhal-online')
def blog_castanhalonline():
    return render_template('blog-castanhalonline.html')

@app.route('/blog/castanhal-mil-grau')
def blog_castanhalmilgrau():
    return render_template('blog-castanhalmilgrau.html')

@app.route('/ZapPessoal')
def zappessoal():
    print("teste")
    return render_template('zappessoal.html')

@app.route('/mobilizar')
def conexoes():
    return render_template('assislink.html')

@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

@app.route('/convite/<identificacao>')
def convite(identificacao):
    return redirect(f"https://api.whatsapp.com/send?phone=559181539406&text=%F0%9F%8E%81%20Quero%20participar%20do%20Doa%C3%A7%C3%A3o%20Premiada%20e%20concorrer%20a%20pr%C3%AAmios%20todo%20m%C3%AAs!%20convite:{identificacao}")

@app.route('/cadastrar/<lider>/<whatsapp>/<dados>/')
def cadastrar(lider,whatsapp,dados):
    lider = lider.replace('%20', ' ')
    if dados == 1 or dados == '1':
        dados = "numero"
    dados = dados.replace('%20', ' ')
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
    try:
        firebase_admin.delete_app(firebase_admin.get_app())
    except:
        pass

    firebase_credentials = os.getenv('FIREBASE_CREDENTIALS')

    cred_dict = json.loads(firebase_credentials)
    cred_obj = firebase_admin.credentials.Certificate(cred_dict)

    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':'https://assistocantinsreserva-default-rtdb.firebaseio.com/'
        })      
    
    ref_usuarios = db.reference(f'/')

    novo_usuario = dados

    ref_usuarios.child(lider).update({
    whatsapp: dados
})

    return f"O {dados} foi adicionado a base de dados!"

if __name__ == '__main__':
    app.run()