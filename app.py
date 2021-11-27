from flask import Flask, render_template, request, redirect, url_for, Response
import json
import sys
import os 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('buscador.html')

@app.route('/resultados')
def result():
   return render_template('resultados.html')


@app.route('/busqueda', methods = ['POST'])
def buscar():

   return Response("Working", status=200, mimetype='application/json')

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))