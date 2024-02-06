from flask import Flask, render_template, url_for, request, redirect
from PIL import Image
import numpy as np
from pickle import load
from re import match
from glob import glob
from os import chdir
import os

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

@app.route('/blog/castanhal-mil-grau')
def blog_milgrau():
    return render_template('blog-castanhalmilgrau.html')

@app.route('/blog/vagas-de-emprego-whatsapp-castanhal')
def vagasdeemprego():
    return render_template('blog-grupodeemprego.html')

@app.route('/blog/castanhal-online')
def blog_castanhalonline():
    return render_template('blog-castanhalonline.html')

@app.route('/ZapPessoal')
def zappessoal():
    return render_template('zappessoal.html')

@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

if __name__ == '__main__':
    app.run()