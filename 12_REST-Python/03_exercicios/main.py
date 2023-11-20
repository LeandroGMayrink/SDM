from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


SALARIO_HORA_NORMAL = 40.0
SALARIO_HORA_EXTRA = 50.0
IMPOSTO_PERCENTUAL = 10


@app.route('/')
def form():
    return render_template('index.html')


@app.route('/calcular_salario', methods=['POST'])
def calcular_salario():
    
    horas_normais = float(request.form['horas_normais'])
    horas_extra = float(request.form['horas_extra'])

    salario_bruto = (horas_normais * SALARIO_HORA_NORMAL) + (horas_extra * SALARIO_HORA_EXTRA)
    imposto = (salario_bruto * IMPOSTO_PERCENTUAL) / 100
    salario_liquido = salario_bruto - imposto

    return render_template('resultado.html', salario_bruto=salario_bruto, salario_liquido=salario_liquido)

if __name__ == '__main__':
    app.run(debug=True)
