from pastebin_api import post_new_paste
from poke_api import search_for_pokemon
import sys

def main():
    name = get_search_term()
    poke_list = search_for_pokemon(name)
    if poke_list:
            title, body_text = get_paste_data(poke_list, name)
            paste_url = post_new_paste(title, body_text, '1M')
            print(f'{paste_url}')

def get_search_term():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing search term')
        sys.exit(1)

def get_paste_data(poke_list, name):

    title = f'"{name}" Abilities'

    divider = '\n' + ('*' * 40) + '\n'
    body_text = divider.join(poke_list)
    return title, body_text


if __name__ == '__main__':
    main()