from flask import Flask, render_template, request, redirect, session
from flask_session import Session
from busca_db import busca_json


sessao = Session()
query = None


class Novocad:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    def registrar(self):
        db = open("users.txt", "a+")
        db.write(f"user: {self.nome}, email: {self.email}, senha: {self.senha}\n")


app = Flask(__name__)


@app.route("/cadastro")
def cadastrar():
    return render_template("cadastro.html", titulo="Cadastro de novo usuário")


@app.route("/retornocad")
def retornarcad():
    return render_template("retornocad.html")


@app.route("/usarionovo", methods=['POST'])    #rota de processamento
def usarionovo():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    novocad = Novocad(nome, email, senha)
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


if __name__ == "__main__":
    app.secret_key = 'vandervilson'
    app.config['SESSION_TYPE'] = 'filesystem'
    sessao.init_app(app)
    app.run(debug=True)