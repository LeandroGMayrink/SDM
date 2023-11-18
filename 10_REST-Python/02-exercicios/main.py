from flask import Flask, render_template, request

app = Flask(__name__)

def obter_preco(codigo):
    precos = {
        1: 'R$ 99,99',
        2: 'R$ 103,89',
        3: 'R$ 49,98',
        4: 'R$ 89,72',
        5: 'R$ 97,35'
    }

    return precos.get(codigo, 'Código de produto inválido')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar_preco', methods=['POST'])
def consultar_preco_route():
    try:
        codigo = int(request.form['codigo'])
        preco = obter_preco(codigo)
        return render_template('resultado.html', preco=preco)
    except ValueError:
        return render_template('resultado.html', preco='Código de produto inválido (não é um número inteiro)')

if __name__ == '__main__':
    app.run(debug=True, port=5000)