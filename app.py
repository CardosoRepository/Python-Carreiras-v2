from flask import Flask, jsonify, render_template

app = Flask(__name__)

VAGAS = [{
    'id': 1,
    'titulo': 'Analista de Dados',
    'localidade': 'SC, Brasil',
    'salario': 'R$ 5.000,00'
}, {
    'id': 2,
    'titulo': 'Desenvolvedor Frontend',
    'localidade': 'PR, Brasil',
    'salario': 'R$ 3.000,00'
}, {
    'id': 3,
    'titulo': 'Cientista de Dados',
    'localidade': 'SP, Brasil',
    'salario': 'R$ 4.000,00'
}, {
    'id': 4,
    'titulo': 'Desenvolvedor Backend',
    'localidade': 'SP, Brasil',
    'salario': 'R$ 5.000,00'
}, {
    'id': 5,
    'titulo': 'Estatítico',
    'localidade': 'RJ, Brasil',
    'salario': 'R$ 3500,00'
}]


@app.route('/')
def hello_world():
    return render_template("home.html", vagas=VAGAS)


@app.route('/vagas')
def vagas():
    return jsonify(VAGAS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
