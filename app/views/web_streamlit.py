import streamlit as st 

def get_user_input():
    """Interface para entrada de dados usando Streamlit."""
    st.title("Gerador de Lore do Batatão")
    game_name = st.text_input("Qual o nome do jogo?", placeholder="Exemplo: Dark Souls")
    place = st.text_input("Qual lugar o Brasil virou?", placeholder="Exemplo: Mordor")
    hero = st.text_input("Qual o herói?", placeholder="Exemplo: Elon Musk")
    enemy = st.text_input("Qual o nome do arqui-inimigo?", placeholder="Exemplo: Mark Zuckerberg")

    return game_name, place, hero, enemy

def display_lore(lore):
    """Exibe a lore gerada na interface Streamlit."""
    st.subheader("Lore Gerada")
    st.write(lore)

def display_error(message):
    """Exibe mensagens de erro na interface Streamlit."""
    st.error(message)

def create_game_card(game_name, game_image, game_description):
    """Cria um card no Streamlit com informações do jogo."""
    with st.container():
        st.image(game_image, width=300, caption=game_name)
        st.subheader(game_name)
        st.write(game_description)


def main():
    """Função principal para a aplicação Streamlit."""
    st.set_page_config(
        page_title="Gerador de Lore do Batatão",
        page_icon="🎮",
        layout="centered",
        initial_sidebar_state="auto",
    )

    game_name, place, hero, enemy = get_user_input()

    if st.button("Gerar Lore"):
        if not game_name or not place or not hero or not enemy:
            display_error("Por favor, preencha todos os campos antes de gerar a lore.")
        else:
            with st.spinner("Gerando ou buscando a lore..."):
                try:
                    from app.controllers.lore_controller import get_lore
                    lore = get_lore(game_name, place, hero, enemy)
                    display_lore(lore)
                except Exception as e:
                    display_error(f"Erro ao gerar a lore: {e}")

if __name__ == "__main__":
    main()
