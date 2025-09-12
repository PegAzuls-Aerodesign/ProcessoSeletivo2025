import requests

def obter_informacoes_pokemon(nome_pokemon):
    """
    Faz uma requisição à PokéAPI para obter informações de um Pokémon específico.
    """
    # Constrói a URL da API para o Pokémon desejado
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon.lower()}"
    
    # Faz a requisição GET
    response = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Converte a resposta para o formato JSON
        dados = response.json()
        
        # Extrai as informações relevantes
        nome = dados['name'].capitalize()
        pokemon_id = dados['id']
        tipos = [tipo['type']['name'].capitalize() for tipo in dados['types']]
        habilidades = [habilidade['ability']['name'].capitalize() for habilidade in dados['abilities']]
        
        # Imprime as informações de forma organizada
        print(f"=============================")
        print(f"Nome: {nome}")
        print(f"ID: {pokemon_id}")
        print(f"Tipos: {', '.join(tipos)}")
        print(f"Habilidades: {', '.join(habilidades)}")
        print(f"=============================\n")
    else:
        print(f"Erro ao buscar informações do Pokémon '{nome_pokemon}'.")
        print(f"Status Code: {response.status_code}\n")

if __name__ == "__main__":
    # Lista de 5 Pokémons para buscar informações
    pokemons_para_buscar = [
        "pikachu",
        "charmander",
        "bulbasaur",
        "squirtle",
        "mewtwo"
    ]
    
    print("Buscando informações de 5 Pokémons...\n")
    
    # Itera sobre a lista e busca as informações de cada um
    for pokemon in pokemons_para_buscar:
        obter_informacoes_pokemon(pokemon)