from flask import  Blueprint, render_template, request


main = Blueprint("routes", __name__)

@main.route("/", methods = ['POST', 'GET'])
def home():
    return render_template("index.html")
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descrição']


@main.route("/contato")
def contato():
    return render_template("contato.html")

@main.route("/quemsomos")
def quemsomos():
    return render_template("quem-somos.html")


