from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

cardapio = {
    1: {"Produto": "Cachorro quente", "Preco": 12.00},
    2: {"Produto": "Sanduíche", "Preco": 23.89},
    3: {"Produto": "Pastel", "Preco": 3.98},
    4: {"Produto": "Refrigerante", "Preco": 5.72},
    5: {"Produto": "Suco", "Preco": 4.35},
}

@app.route('/')
def mostrar_index():
    return render_template('index.html')

@app.route('/cardapio', methods=['GET'])
def consultar_cardapio():
    return jsonify({"cardapio": cardapio})

@app.route('/cardapio/<int:codigo>', methods=['GET'])
def consultar_item(codigo):
    if codigo in cardapio:
        return jsonify({"item": cardapio[codigo]})
    else:
        return jsonify({"message": "Item não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
