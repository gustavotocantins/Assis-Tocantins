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
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/whatsapp')
def whatsapp():
    return redirect('https://chat.whatsapp.com/Ghx4tk2ApIw9A9WNTklIYF')

if __name__ == '__main__':
    app.run()