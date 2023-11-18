from flask import Flask, render_template, request

app = Flask(__name__)

def verificar_triangulo(x, y, z):
    if x < y + z and y < x + z and z < x + y:
        return 'Os valores podem ser os comprimentos dos lados de um triângulo.'
    else:
        return 'Os valores NÃO podem ser os comprimentos dos lados de um triângulo.'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verificar_triangulo', methods=['POST'])
def verificar_triangulo_route():
    x = float(request.form['x'])
    y = float(request.form['y'])
    z = float(request.form['z'])
    
    resultado = verificar_triangulo(x, y, z)
    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
