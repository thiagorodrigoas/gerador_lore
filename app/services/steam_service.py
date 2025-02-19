import requests

STEAM_BASE_URL = "https://store.steampowered.com/api/appdetails"

def get_game_description(game_name):
    """Obtém a descrição de um jogo da Steam pelo nome."""
    # Busca o ID do jogo pela SteamDB ou similar (simplificado aqui)
    search_url = f"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(search_url)
    response.raise_for_status()

    games = response.json()["applist"]["apps"]
    
    game_id_list = list((game["appid"] for game in games if game_name.lower() in game["name"].lower()))
    
    game_id = min(game_id_list)
    if not game_id:
        return None, "Jogo não encontrado."

    # Obtém detalhes do jogo
    params = {"appids": game_id}
    response = requests.get(STEAM_BASE_URL, params=params)
    response.raise_for_status()

    game_data = response.json().get(str(game_id), {}).get("data", {})

    if not game_data or "short_description" not in game_data:
        return None, "Descrição não disponível para este jogo."
    
    game_data_filter = {
        "game_id": game_data.get("game_id"),
        "name": game_data.get("name"),
        "header_image": game_data.get("header_image"),
        "short_description": game_data.get("short_description")
    }
    return game_data_filter, None
