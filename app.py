
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hola, MUNDO!</p>"

@app.route("/chau")
def bye():
    return "<p>Chau, MUNDO!</p>"

@app.route("/Saludar/por-nombre/<string:nombre>")
def sxn (Nombre):
    return "<p>Hola{Nombre}<p>"

@app.route("/Sumar/<int:n1/<int:n2>")
def sum (n1,n2):
    return f"<p>{n1} + {n2} = {s}<p>"

@app.route("/Tirar/dados/<int:caras>")
def dados (Caras):
    from random import randint
    n=randint(Caras)
    return f"<p>Tire un dado de{Caras} caras, salio {n}<p>"