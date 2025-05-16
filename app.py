from flask import Flask, jsonify, render_template, request
from database import carrega_vagas_db, carrega_vaga_db, cria_tabelas, adiciona_inscricao

app = Flask(__name__)

cria_tabelas()

@app.route('/')
def hello_world():
    vagas = carrega_vagas_db()
    return render_template("home.html", vagas=vagas)


@app.route('/vagas')
def vagas():
    vagas = carrega_vagas_db()
    return jsonify(vagas)

@app.route('/vaga/<id>')
def mostra_vaga(id):
    vaga = carrega_vaga_db(id)
    if not vaga:
        return 'Not Found', 404
    
    return render_template('detalhe_vaga.html', vaga=vaga)

@app.route('/vaga/<id>/inscricao', methods=['GET', 'POST'])
def inscricao_vaga(id):
    vaga = carrega_vaga_db(id)
    formulario = request.form
    adiciona_inscricao(id, formulario)
    return render_template('inscricao_concluida.html', inscricao=formulario, vaga=vaga)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
