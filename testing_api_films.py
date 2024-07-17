import requests


def get_character_names_with_darth_vader() -> set:
    """Возвращает множество имен персонажей, которые снимались в фильмах с Дарт Вейдером."""
    response = requests.get("https://swapi.dev/api/people/4/")
    if response.status_code != 200:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return set()

    films_urls = response.json().get('films', [])
    character_names = set()

    for film_url in films_urls:
        film_response = requests.get(film_url)
        characters_urls = film_response.json().get('characters', [])
        for character_url in characters_urls:
            character_response = requests.get(character_url)
            if character_response.status_code == 200:
                character_names.add(character_response.json().get('name', ''))

    return character_names


def save_names_to_file(names: set, filename: str) -> None:
    """Сохраняет имена персонажей в файл"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(names) + '\n')


character_names = get_character_names_with_darth_vader()
save_names_to_file(character_names, 'characters_with_darth_vader.txt')

