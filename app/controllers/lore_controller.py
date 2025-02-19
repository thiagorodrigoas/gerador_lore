from app.models.database import save_lore, get_lore
from app.services.steam_service import get_game_description
from app.services.groq_service import generate_lore
# from app.views.console import get_user_input, display_lore, display_error
from app.views.web_streamlit import main, get_user_input, display_lore, display_error, create_game_card

def generate_and_save_lore():
    main()
    game_name, place, hero, enemy = get_user_input()

    print("Buscando descrição do jogo na Steam...")
    game_info, error = get_game_description(game_name)

    if error:
        display_error(error)
        return
    
    create_game_card(**game_info)

    game_description = game_info['short_description']
    print("Gerando a lore...")
 
    lore = get_lore(game_name, place, hero, enemy)
    if not lore:  
        lore = generate_lore(game_name, place, hero, enemy, game_description)
        save_lore(game_name, place, hero, enemy, lore)

    display_lore(lore)
    print("Lore salva no banco de dados com sucesso!")
