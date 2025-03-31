
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hola, MUNDO!</p>"

@app.route("/chau")
def bye():
    return "<p>Chau, MUNDO!</p>"
