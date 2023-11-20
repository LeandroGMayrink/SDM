from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('produtos.db')
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

def conectar_bd():
    return sqlite3.connect('produtos.db')

conn = conectar_bd()
cursor = conn.cursor()
cursor.executemany('INSERT INTO produtos (nome, preco) VALUES (?, ?)', [
    ('sapato', 128.55),
    ('camisa', 49.89),
    ('calça', 89.99),
    ('bermuda', 78.63)
])
conn.commit()
conn.close()

# http://127.0.0.1:5000/produtos
@app.route('/produtos', methods=['GET'])
def retornar_todos_os_produtos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = [{'id': row[0], 'nome': row[1], 'preco': row[2]} for row in cursor.fetchall()]
    conn.close()

    resp = produtos
    if 'X-nome-produto' in request.headers:
        nome = request.headers['X-nome-produto']
        for produto in produtos:
            if produto['nome'] == nome:
                resp = produto
    return jsonify(resp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
