from groq import Groq

GROQ_API_KEY = "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"

def generate_lore(game_name, place, hero, enemy, game_description):
    """Gera a lore divertida usando a API do ChatGPT."""
    client = Groq(
        api_key = GROQ_API_KEY,  # This is the default and can be omitted
    )

    prompt = f'''Crie uma história fictícia, divertida e baseada em um cenário exagerado e caricatural onde o herói deve enfrentar um grande vilão para salvar o mundo ou sua pátria. Personalize o texto com os seguintes elementos fornecidos:
            Nome do jogo/tema : {game_name}
            Descrição do jogo: {game_description}
            Lugar que o Brasil virou: {place}
            Nome do herói: {hero}
            Nome do arqui-inimigo: {enemy}
            Estrutura do texto:
            O Brasil virou a(o) 'local', 'herói' (com seus adjetivos improváveis) deve enfrentar (crie inimigos subordinados do jogo e relacione ao 'arqui-inimigo'). Será que 'herói' vai conseguir?'''
 
    sys_content = '''O texto deve:
            seguir a estrutura das 4 frases e ser e engraçado.
            Conter adjetivos positivos improvaveis ao herói e negativos ao vilão.
            Fazer referências criativas e engraçadas com a descrição do jogo.
            Conter elementos de humor, como exageros caricatos e comparações inusitadas.
            Evitar revelar o desfecho da história, finalizando com uma pergunta provocativa que convida o leitor a imaginar o que acontecerá a seguir.'''

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": sys_content},
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_completion_tokens=300,
        top_p=0.9,
        stream=False    
    )
    return response.choices[0].message.content
