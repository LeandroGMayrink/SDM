from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def conectar_bd():
    return sqlite3.connect('produtos.db')

def criar_tabela():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco REAL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_produtos_iniciais():
    produtos_iniciais = [
        ('sapato', 128.55),
        ('camisa', 49.89),
        ('calça', 89.99),
        ('bermuda', 78.63)
    ]

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM produtos')
    count = cursor.fetchone()[0]

    if count == 0:
        for produto in produtos_iniciais:
            cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', produto)

    conn.commit()
    conn.close()

criar_tabela()
adicionar_produtos_iniciais()

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = [{'id': row[0], 'nome': row[1], 'preco': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify({'produtos': produtos})

# http://127.0.0.1:5000/produtos/camisa/10.00
# http://127.0.0.1:5000/produtos/camisa/-10.00
@app.route('/produtos/<string:nome>/<float(signed=t):preco>', methods=['PATCH'])
def alterar_preco_do_produto(nome, preco):
    if preco < 0:
        return jsonify({'erro': 'O preço não pode ser negativo'}), 400

    conn = conectar_bd()
    cursor = conn.cursor()

    cursor.execute('UPDATE produtos SET preco = ? WHERE nome = ?', (preco, nome))
    conn.commit()
    conn.close()

    return jsonify({'produto': nome, 'novo_preco': preco})


# http://127.0.0.1:5000/produtos/camisa
@app.route('/produtos/<string:nome>', methods=['GET'])
def retornar_dados_do_produto_informado(nome):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos WHERE nome = ?', (nome,))
    produto = cursor.fetchone()
    conn.close()

    if produto:
        return jsonify({'produto': produto[1], 'preco': produto[2]})
    else:
        return jsonify({'mensagem': f'Produto {nome} não encontrado'}), 404

# http://127.0.0.1:5000/produtos/cinto/45.67
@app.route('/produtos/<string:nome>/<float:preco>', methods=['POST'])
def inserir_produto(nome, preco):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
    conn.commit()
    conn.close()
    return jsonify({'produto': nome, 'preco': preco})

# http://127.0.0.1:5000/produtos/camisa
@app.route('/produtos/<string:nome>', methods=['DELETE'])
def remover_produto(nome):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE nome = ?', (nome,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': f'Produto {nome} removido com sucesso'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
