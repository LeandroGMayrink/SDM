from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = False 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar_numeros', methods=['POST'])
def processar_numeros():
    try:
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        numero3 = float(request.form['numero3'])

        menor = min(numero1, numero2, numero3)
        maior = max(numero1, numero2, numero3)
        media = (numero1 + numero2 + numero3) / 3

        return render_template('resultado.html', menor=menor, maior=maior, media=media)
    except ValueError:
        return render_template('resultado.html', erro='Erro ao processar números (não são valores numéricos)')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
