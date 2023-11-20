from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

PRECO_PEQUENA = 10.0
PRECO_MEDIA = 12.0
PRECO_GRANDE = 15.0

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/calcular_valor', methods=['POST'])
def calcular_valor():

    qtd_pequena = int(request.form['pequena'])
    qtd_media = int(request.form['media'])
    qtd_grande = int(request.form['grande'])

    valor_total = (qtd_pequena * PRECO_PEQUENA) + (qtd_media * PRECO_MEDIA) + (qtd_grande * PRECO_GRANDE)

    return render_template('resultado.html', valor_total=valor_total)

if __name__ == '__main__':
    app.run(debug=True)
