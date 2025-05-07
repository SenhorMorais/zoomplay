from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco
def connect_db():
    return sqlite3.connect('zoomplay.db')

# Página inicial com busca
@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('search', '')
    conn = connect_db()
    if query:
        filmes = conn.execute('SELECT * FROM filmes WHERE nome LIKE ?', ('%' + query + '%',)).fetchall()
        series = conn.execute('SELECT * FROM series WHERE nome LIKE ?', ('%' + query + '%',)).fetchall()
    else:
        filmes = conn.execute('SELECT * FROM filmes').fetchall()
        series = conn.execute('SELECT * FROM series').fetchall()
    conn.close()
    return render_template('index.html', filmes=filmes, series=series, search=query)

# Página de filmes
@app.route('/filmes')
def filmes():
    conn = connect_db()
    filmes = conn.execute('SELECT * FROM filmes').fetchall()
    conn.close()
    return render_template('filmes.html', filmes=filmes)

# Página de séries
@app.route('/series')
def series():
    conn = connect_db()
    series = conn.execute('SELECT * FROM series').fetchall()
    conn.close()
    return render_template('series.html', series=series)

# Página de lançamentos (exibe ambos)
@app.route('/lancamentos')
def lancamentos():
    conn = connect_db()
    filmes = conn.execute('SELECT * FROM filmes ORDER BY id DESC LIMIT 2').fetchall()
    series = conn.execute('SELECT * FROM series ORDER BY id DESC LIMIT 2').fetchall()
    conn.close()
    return render_template('lancamentos.html', filmes=filmes, series=series)

# Página de reprodução
@app.route('/play/<tipo>/<int:item_id>')
def play(tipo, item_id):
    conn = connect_db()
    if tipo == 'filme':
        item = conn.execute('SELECT * FROM filmes WHERE id = ?', (item_id,)).fetchone()
    elif tipo == 'serie':
        item = conn.execute('SELECT * FROM series WHERE id = ?', (item_id,)).fetchone()
    else:
        item = None
    conn.close()
    if not item:
        return "Conteúdo não encontrado", 404
    return render_template('play.html', item=item)

# Rodar servidor
if __name__ == '__main__':
    app.run(debug=True)
