import csv
import json
import os
import requests

SPRITE_PAGES = {
    '1': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-1-r128/',
    '2': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-2-r129/',
    '3': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-3-r130/',
    '4': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-4-r131/',
    '5': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-5-r132/',
    '6': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-6-r133/',
    '7': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-7-r134/',
    '8': 'https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-8-r135/',
}


def get_html(url):
    print('\tGetting HTML from %s' % url)
    r = requests.get(url)
    return r.text


def parse_html(generation, html):
    data = []
    datum = {}
    lines = html.splitlines()
    print('\tParsing %d lines of HTML...' % len(lines))

    for line in lines:
        line = line.strip()

        if line.startswith('<img') and 'src="https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_' in line:

            imageUrl = line.split('src="')[1].split('"></td>')[0]

            id = imageUrl.split(
                'https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_')[1][0:4]

            if id in datum.keys():
                datum[id].append(imageUrl)
            else:
                datum[id] = [imageUrl]
    return datum


def main():
    data = {}
    for generation in SPRITE_PAGES:

        sprite_page_url = SPRITE_PAGES[generation]
        print('\nProcessing sprites for Pokemon Generation %s...' % generation)

        html = get_html(sprite_page_url)
        data.update(parse_html(generation, html))

    with open("sprites.json", "a") as outfile:  
        json.dump(data, outfile) 

    print('\nDone!')


if __name__ == "__main__":
    main()
