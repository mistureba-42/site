from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home</h1>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    produtos = {
        ("nome": "coca": "descrição": "bom"),
        ("nome": "guarana": "descrição": "o melhor"),
        ("nome": "pepsi": "descrição": "ruim"),
    }

    return render_template("produtos.html", produtos = produtos)

@app.route("/produtos/<nome>")
def produtos(nome):
    return nome