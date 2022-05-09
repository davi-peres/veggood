from flask import Flask, render_template, request, redirect, session, flash
from flask_session import Session
from busca_db import busca_json


sessao = Session()
query = None


class Novocad:
    def __init__(self, nomesobrenome, email, telefone, cep, endereco, numero, cidade, complemento):
        self.nomesobrenome = nomesobrenome
        self.email = email
        self.telefone = telefone
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.cidade = cidade
        self.complemento = complemento

    def registrar(self):
        db = open("users.txt", "a+")
        db.write(f"user: {self.nomesobrenome}, email: {self.email}, telefone: {self.telefone}, cep: {self.cep}"
                 f", endereco: {self.endereco}, numero: {self.numero}, cidade: {self.cidade}, complemento: {self.complemento}\n")


class Mensagem:
    def __init__(self, nomesobrenome, email, telefone, mensagem):
        self.nomesobrenome = nomesobrenome
        self.email = email
        self.telefone = telefone
        self.mensagem = mensagem

    def registrar_msg(self):
        db = open("mensagem.txt", "a+")
        db.write(f"Nome e sobrenome: {self.nomesobrenome}, Email: {self.email}, "
                 f"Telefone: {self.telefone}\n, Mensagem: {self.mensagem}\n")


app = Flask(__name__)


@app.route("/cadastro")
def cadastrar():
    return render_template("cadastro.html")


@app.route("/retornocad")
def retornarcad():
    return render_template("retornocad.html")


@app.route("/usarionovo", methods=['POST'])    #rota de processamento de cadastro
def usarionovo():
    nomesobrenome = request.form['nomesobrenome']
    email = request.form['email']
    telefone = request.form['telefone']
    cep = request.form['cep']
    endereco = request.form['endereco']
    numero = request.form['numero']
    cidade = request.form['cidade']
    complemento = request.form['complemento']
    novocad = Novocad(nomesobrenome, email, telefone, cep, endereco, numero, cidade, complemento)
    novocad.registrar()
    return redirect('retornocad')


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/msgenviada", methods=['POST']) #rota de processamento mensagem
def envia_msg():
    nome = request.form['nomesobrenome']
    email = request.form['email']
    telefone = request.form['telefone']
    mensagem = request.form['mensagem']
    msg = Mensagem(nome, email, telefone, mensagem)
    msg.registrar_msg()
    flash("Mensagem enviada com sucesso!")
    return redirect('contato')


@app.route("/resultadobusca", methods=['POST'])
def resultado():
    query = request.form['pesquisa']
    session['url'] = query
    url_query = busca_json(query)
    if url_query:
        return render_template("resultados.html", data=query, url=url_query)
    return render_template("resultados.html", data="Resultado não encontrado.")


@app.route("/link", methods=['GET'])  #rota redirecionamento
def link():
    url = session.get('url', None)
    url_query = busca_json(url)
    if url_query:
        return redirect(url_query)
    else:
        return render_template("index.html")


@app.route("/clubevegano")
def clube_vegano():
    return render_template("clube-vegano.html")


@app.route("/veggiesabor")
def veggie_sabor():
    return render_template("veggie-sabor.html")


@app.route("/vidavegana")
def vida_vegana():
    return render_template("vida-vegana.html")


if __name__ == "__main__":
    app.secret_key = 'vandervilson'
    app.config['SESSION_TYPE'] = 'filesystem'
    sessao.init_app(app)
    app.run(debug=True)