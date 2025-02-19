import duckdb
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'lore_generator.duckdb')

def initialize_database():
    """Inicializa o banco de dados e cria as tabelas necessárias."""
    conn = duckdb.connect(DB_PATH)
    conn.execute('''
        CREATE SEQUENCE IF NOT EXISTS id_sequence START 1;
        CREATE TABLE IF NOT EXISTS lories (
            id INTEGER DEFAULT nextval('id_sequence'),
            game_name VARCHAR,
            img_game_link VARCHAR,
            short_description TEXT,
            place VARCHAR,
            hero VARCHAR,
            enemy VARCHAR,
            lore TEXT,
            --like INTEGER,
            --dislike INTEGER,
            dat_create TIMESTAMP DEFAULT current_localtimestamp()
        );
    ''')
    conn.close()

def save_lore(game_name,img_game_link, short_description, place, hero, enemy, lore):
    """Salva a lore gerada no banco de dados."""
    conn = duckdb.connect(DB_PATH)
    conn.execute('''
        INSERT INTO lories (game_name, img_game_link,short_description, place, hero, enemy, lore)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (game_name, img_game_link, short_description, place, hero, enemy, lore))
    conn.close()

def get_lore(game_name, place, hero, enemy):
    """Gera ou busca a lore com base nos parâmetros fornecidos."""
    # Verifica se já existe uma lore no banco de dados
    conn = duckdb.connect(DB_PATH)
    result = conn.execute('''
        SELECT lore FROM lories
        WHERE game_name = ? AND place = ? AND hero = ? AND enemy = ?
    ''', (game_name, place, hero, enemy)).fetchone()

    conn.close()

    if result:
        conn.close()
        return result[0]  # Retorna a lore existente
    else:
        return False
        
 

