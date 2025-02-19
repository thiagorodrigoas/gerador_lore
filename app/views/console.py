def get_user_input():
    """Obtém as entradas do usuário para criar a lore."""
    game_name = input("Qual o nome do jogo? ")
    place = input("Qual lugar o Brasil virou? ")
    hero = input("Qual o nome do herói? ")
    enemy = input("Qual o nome do arqui-inimigo? ")
    return game_name, place, hero, enemy

def display_lore(lore):
    """Exibe a lore gerada."""
    print("\n--- Lore Gerada ---\n")
    print(lore)

def display_error(message):
    """Exibe mensagens de erro."""
    print(f"Erro: {message}")
