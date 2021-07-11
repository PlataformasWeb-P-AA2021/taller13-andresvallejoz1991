from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Bienvenidos a la Aplicacións!</p>"
 

@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8081/api/edificios/",
            auth=('andrew', 'noletudo'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)



@app.route("/losdepas")
def los_depas():
    """
    """
    r = requests.get("http://127.0.0.1:8081/api/departamentos/",
            auth=('andrew', 'noletudo'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombre_pro':d['nombre_pro'], 'costo_depar':d['costo_depar'],'numero_cuar':d['numero_cuar'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepas.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('andrew', 'noletudo'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
