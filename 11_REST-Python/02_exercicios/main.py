from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def mostrar_formulario():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular_e_mostrar_resultado():
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])

    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    return render_template('resultado.html', distancia=distancia)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
