import flask
app = flask.Flask(__name__)
@app.route('/saudacao/<Robson>')
def saudar(Robson):
    return f'Olá, {Robson}'

@app.route('/sobre/<Robson>')
def sobre(Robson):
    return '<h1>Sobre mim</h1><p>Sou um Oficial de Manutenção</p>'
if __name__ == '__main__':
    app.run(debug=True)