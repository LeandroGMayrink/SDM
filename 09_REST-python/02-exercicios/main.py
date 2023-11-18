from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    try:
        peso = float(request.form['peso'])
        altura_cm = float(request.form['altura'])

        altura_m = altura_cm / 100.0

        imc = peso / (altura_m ** 2)
        classificacao = classificar_imc(imc)

        return render_template('resultado.html', imc=imc, classificacao=classificacao)
    except ValueError:
        return render_template('resultado.html', erro='Erro ao processar os dados. Certifique-se de inserir números válidos.')

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc <= 24.9:
        return 'Peso ideal (parabéns)'
    elif 25.0 <= imc <= 29.9:
        return 'Levemente acima do peso'
    elif 30.0 <= imc <= 34.9:
        return 'Obesidade grau I'
    elif 35.0 <= imc <= 39.9:
        return 'Obesidade grau II (severa)'
    else:
        return 'Obesidade grau III (mórbida)'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
