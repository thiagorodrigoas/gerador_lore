from flask import Flask, render_template, request
from services.steam_service import get_game_description
from services.groq_service import generate_lore
from models.database import save_lore, get_lore, initialize_database, DB_PATH
import os
 
class MyFlaskApp:
    def __init__(self):
        # Inicializa a aplicação do Flask
        self.app = Flask(__name__)
        self.app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

        #Define variaveis para a aplicação 
        self.game_data = {}
        self.game_lore = {}
        
        
        # Define uma rota simples para o índice
        self.app.add_url_rule('/', 'index', self.index, methods=['GET', 'POST'])
        self.app.add_url_rule('/gera_lore', 'gera_lore', self.gera_lore, methods=['GET', 'POST'])
        # self.app.add_url_rule('/sobre', 'sobre', self.sobre)
    
    def index(self):
        if request.method == 'POST':
            nome_jogo = request.form.get('nomeJogo', '')

            self.game_data, erro = get_game_description(nome_jogo.lower())
            print(self.game_data, erro , sep='\n')
        return render_template('index.html', game_data=self.game_data)


    def gera_lore(self): 

        if request.method == 'POST':
            name = self.game_data.get('name')
            img_game_link = self.game_data.get('header_image')
            short_description = self.game_data.get('short_description')
            place = request.form.get('brasilVirou', '')
            hero = request.form.get('heroi', '')
            enemy = request.form.get('arquiInimigo', '')

        lore = get_lore(name, place, hero, enemy)
        if not lore: 
            lore = generate_lore(game_name=name,
                                           place=place,
                                           hero=hero,
                                           enemy=enemy,
                                           game_description=short_description)
            save_lore(name, img_game_link, short_description, place, hero, enemy, lore)

        self.game_lore['lore'] = lore
        self.game_lore['place'] = place
        self.game_lore['hero'] = hero
        self.game_lore['enemy'] = enemy

        return render_template('index.html', game_lore=self.game_lore, game_data=self.game_data)

    # def sobre(self):
    #     return render_template('sobre.html')

    def run(self):
        # Método que executa a aplicação
        self.app.run(debug=True)

if __name__ == '__main__':
    app = MyFlaskApp()
    if not os.path.exists(DB_PATH):
        initialize_database()
    app.run(host="0.0.0.0", debug=True)
