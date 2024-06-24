from flask import Flask, render_template, request, redirect, url_for
from validate_docbr import CPF, CNPJ

app = Flask(__name__)

lista_produtos = [
    ("nome", "coca-cola", "refrigerante doce")
    ("doritos", "salgadinho farelento")
    ("agua", "o mais saudavel")
]

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
    for produto in lista_produtos:
        if produto["nome"] == nome:
            return render_template("produto.html", produto=produto)

    return "produto nao existe"

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos", method=["POST"])
def salvar_produto():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = request.form["preco"]
    imagem = request.form["imagem"]

    produto = {"nome" : nome, "descricao" : descricao, "preco" : preco, "imagem": imagem}
    lista_produtos.append(produto)


    return redirect(url_for("produtos"))

@app.route("/Gerar_CPF")
def gerar_cpf():
    cpf = CPF()
    new_cpf = cpf.generate()

    return "<h1>{{cpf}}</h1>"

@app.route("/Gerar_CNPJ")
def gerar_cpf():
    cnpj = CNPJ()
    new_cnpj = cnpj.generate()

    return "<h1>{{cnpj}}</h1>"

@app.route("/Validar_CPF", method=["POST"])
def validar_cpf():
    cpf = request.form["cpf"]

    cpf = CPF()
    cpf.validate()    

    return "<h1>{{cpf.validate}}</h1>"

@app.route("/Validar_CNPJ", method=["POST"])
def validar_cnpj():
    cnpj = request.form["cnpj"]

    cnpj = CNPJ()
    cnpj.validate()

    return "<h1>{{cnpj.validate}}</h1>"