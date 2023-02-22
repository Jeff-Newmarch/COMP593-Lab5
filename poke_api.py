import requests
from sys import argv
POKEMON_API_URL = 'https://pokeapi.co/api/v2/pokemon/'


def main():
    name = argv[1]
    poke_list = search_for_pokemon(name)
    print(*poke_list)
    return


def search_for_pokemon(name):

    # Send the GET request to the PokeAPI
    print(f'Getting information for {name} ...', end='')
    resp_msg = requests.get(POKEMON_API_URL)
    
    #Check whether the GET request was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        poke_list = [p['name'] for p in body_dict['results']]
        return poke_list
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        print(f'Reason: {resp_msg.text}')

    return

if __name__ == '__main__':
    main()