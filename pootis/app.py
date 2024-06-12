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

    return render_template("produtos.html", produtos = produtos)

@app.route("/produtos/<nome>")
def produtos(nome):
    for produto in lista_de_produtos:
        if produto["nome"] == nome:
            return render_template("produto.html", produto=produto)

    return "produto nao existe"