import sqlite3

conn = sqlite3.connect('zoomplay.db')
cursor = conn.cursor()

# Tabela de filmes
cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    imagem_url TEXT NOT NULL,
    video_url TEXT NOT NULL
)
''')

# Tabela de séries
cursor.execute('''
CREATE TABLE IF NOT EXISTS series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    imagem_url TEXT NOT NULL,
    video_url TEXT NOT NULL
)
''')

# Inserir alguns dados de exemplo
cursor.executemany('INSERT INTO filmes (nome, imagem_url, video_url) VALUES (?, ?, ?)', [
    ("Filme Exemplo 1", "https://via.placeholder.com/300x450?text=Filme+1", "https://www.w3schools.com/html/mov_bbb.mp4"),
    ("Filme Exemplo 2", "https://via.placeholder.com/300x450?text=Filme+2", "https://www.w3schools.com/html/movie.mp4")
])

cursor.executemany('INSERT INTO series (nome, imagem_url, video_url) VALUES (?, ?, ?)', [
    ("Série Exemplo 1", "https://via.placeholder.com/300x450?text=Série+1", "https://www.w3schools.com/html/mov_bbb.mp4"),
    ("Série Exemplo 2", "https://via.placeholder.com/300x450?text=Série+2", "https://www.w3schools.com/html/movie.mp4")
])

conn.commit()
conn.close()

print("Banco de dados criado com sucesso.")
