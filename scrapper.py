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

# hellow world this is absolute bullshit and we all kjnejnwejn


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

            apiId = int(id)
            apiUrl = 'https://pokeapi.co/api/v2/pokemon/'+str(apiId)

            if id in datum.keys():
                # ShinyMale
                if "_md_" in imageUrl and "_r." in imageUrl:
                    if "ShinyMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # ShinyFemale
                if "_fd_" in imageUrl and "_r." in imageUrl:
                    if "ShinyFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyFemale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalMale
                if "_md_" in imageUrl and "_n." in imageUrl:
                    if "NormalMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalFemale
                if "_fd_" in imageUrl and "_n." in imageUrl:
                    if "NormalFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalFemale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # GigaNormal
                if "_g_" in imageUrl and "_n." in imageUrl:
                    if "GigaNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaNormal"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # GigaShiny
                if "_g_" in imageUrl and "_r." in imageUrl:
                    if "GigaShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaShiny"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NoGenShiny
                if "_mf_" in imageUrl and "_r." in imageUrl:
                    if "NoGenShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenShiny"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NoGenNormal
                if "_mf_" in imageUrl and "_n." in imageUrl:
                    if "NoGenNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenNormal"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # Misc
                # elif "_md_" not in imageUrl and "_fd_" not in imageUrl and "_mf_" not in imageUrl:
                else:
                    datum[id]["Sprites"]["Misc"].append(imageUrl)

                # print(json.dumps(datum[id],sort_keys=True, indent=4))

            else:
                pokemonName = requests.get(apiUrl).json()["name"]
                datum[id] = {}
                datum[id]["Name"] = pokemonName
                datum[id]["Sprites"] = {}
                datum[id]["Sprites"]["Misc"] = []
                # ShinyMale
                if "_md_" in imageUrl and "_r." in imageUrl:
                    if "ShinyMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # ShinyFemale
                if "_fd_" in imageUrl and "_r." in imageUrl:
                    if "ShinyFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyFemale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalMale
                if "_md_" in imageUrl and "_n." in imageUrl:
                    if "NormalMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalFemale
                if "_fd_" in imageUrl and "_n." in imageUrl:
                    if "NormalFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalFemale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # GigaNormal
                if "_g_" in imageUrl and "_n." in imageUrl:
                    if "GigaNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaNormal"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # GigaShiny
                if "_g_" in imageUrl and "_r." in imageUrl:
                    if "GigaShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaShiny"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NoGenShiny
                if "_mf_" in imageUrl and "_r." in imageUrl:
                    if "NoGenShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenShiny"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NoGenNormal
                if "_mf_" in imageUrl and "_n." in imageUrl:
                    if "NoGenNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenNormal"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # Misc
                # elif "_md_" not in imageUrl and "_fd_" not in imageUrl and "_mf_" not in imageUrl:
                else:
                    datum[id]["Sprites"]["Misc"].append(imageUrl)

    return datum


def parse_Json():
    data = []
    datum = {}

    with open('sprites.json') as f:
        Jsondata = json.load(f)

    c = 0
    for id in Jsondata:

        Jsondata[id]["Sprites"].sort()
        for imageUrl in Jsondata[id]["Sprites"]:
            if id in datum.keys():

                # ShinyMale
                if "_md_" in imageUrl and "_f_r." in imageUrl:
                    if "ShinyMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyMale"] = imageUrl

                # ShinyFemale
                if "_fd_" in imageUrl and "_f_r." in imageUrl:
                    if "ShinyFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyFemale"] = imageUrl

                # NormalMale
                if "_md_" in imageUrl and "_f_n." in imageUrl:
                    if "NormalMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalMale"] = imageUrl

                # NormalFemale
                if "_fd_" in imageUrl and "_f_n." in imageUrl:
                    if "NormalFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalFemale"] = imageUrl

                # GigaNormal
                if "_g_" in imageUrl and "_f_n." in imageUrl:
                    if "GigaNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaNormal"] = imageUrl

                # GigaShiny
                if "_g_" in imageUrl and "_f_r." in imageUrl:
                    if "GigaShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaShiny"] = imageUrl

                # NoGenNormal
                if "_mf_" in imageUrl and "_f_n." in imageUrl:
                    if "NoGenNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenNormal"] = imageUrl

                # NoGenShiny
                if "_mf_" in imageUrl and "_f_r." in imageUrl:
                    if "NoGenShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenShiny"] = imageUrl

                # MaleOnlyNormal
                if "_mo_" in imageUrl and "_f_n." in imageUrl:
                    if "MaleOnlyNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["MaleOnlyNormal"] = imageUrl

                # FemaleOnlyNormal
                if "_fo_" in imageUrl and "_f_n." in imageUrl:
                    if "FemaleOnlyNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["FemaleOnlyNormal"] = imageUrl

                # MaleOnlyShiny
                if "_mo_" in imageUrl and "_f_r." in imageUrl:
                    if "MaleOnlyShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["MaleOnlyShiny"] = imageUrl

                # FemaleOnlyShiny
                if "_fo_" in imageUrl and "_f_r." in imageUrl:
                    if "FemaleOnlyShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["FemaleOnlyShiny"] = imageUrl

                # UnknownShiny
                if "_uk_" in imageUrl and "_f_r." in imageUrl:
                    if "UnknownShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["UnknownShiny"] = imageUrl

                # UnknownNormal
                if "_uk_" in imageUrl and "_f_n." in imageUrl:
                    if "UnknownNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["UnknownNormal"] = imageUrl
                # Misc
                else:
                    if imageUrl not in datum[id]["Sprites"]["Misc"]:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # print(json.dumps(datum[id],sort_keys=True, indent=4))
            # NormalMale
            # ShinyMale
            
            # NormalFemale
            # ShinyFemale
            
            # GigaNormal
            # GigaShiny

            # NoGenNormal
            # NoGenShiny

            # MaleOnlyNormal
            # MaleOnlyShiny

            # FemaleOnlyNormal
            # FemaleOnlyShiny

            # UnknownNormal
            # UnknownShiny

            else:
                pokemonName = Jsondata[id]["Name"]
                datum[id] = {}
                datum[id]["Name"] = pokemonName
                datum[id]["Sprites"] = {}
                datum[id]["Sprites"]["Misc"] = []

                # ShinyMale
                if "_md_" in imageUrl and "_f_r." in imageUrl:
                    if "ShinyMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyMale"] = imageUrl

                # ShinyFemale
                if "_fd_" in imageUrl and "_f_r." in imageUrl:
                    if "ShinyFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyFemale"] = imageUrl

                # NormalMale
                if "_md_" in imageUrl and "_f_n." in imageUrl:
                    if "NormalMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalMale"] = imageUrl

                # NormalFemale
                if "_fd_" in imageUrl and "_f_n." in imageUrl:
                    if "NormalFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalFemale"] = imageUrl

                # GigaNormal
                if "_g_" in imageUrl and "_f_n." in imageUrl:
                    if "GigaNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaNormal"] = imageUrl

                # GigaShiny
                if "_g_" in imageUrl and "_f_r." in imageUrl:
                    if "GigaShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["GigaShiny"] = imageUrl

                # NoGenNormal
                if "_mf_" in imageUrl and "_f_n." in imageUrl:
                    if "NoGenNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenNormal"] = imageUrl

                # NoGenShiny
                if "_mf_" in imageUrl and "_f_r." in imageUrl:
                    if "NoGenShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenShiny"] = imageUrl

                # MaleOnlyNormal
                if "_mo_" in imageUrl and "_f_n." in imageUrl:
                    if "MaleOnlyNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["MaleOnlyNormal"] = imageUrl

                # FemaleOnlyNormal
                if "_fo_" in imageUrl and "_f_n." in imageUrl:
                    if "FemaleOnlyNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["FemaleOnlyNormal"] = imageUrl

                # MaleOnlyShiny
                if "_mo_" in imageUrl and "_f_r." in imageUrl:
                    if "MaleOnlyShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["MaleOnlyShiny"] = imageUrl

                # FemaleOnlyShiny
                if "_fo_" in imageUrl and "_f_r." in imageUrl:
                    if "FemaleOnlyShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["FemaleOnlyShiny"] = imageUrl

                # UnknownShiny
                if "_uk_" in imageUrl and "_f_r." in imageUrl:
                    if "UnknownShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["UnknownShiny"] = imageUrl

                # UnknownNormal
                if "_uk_" in imageUrl and "_f_n." in imageUrl:
                    if "UnknownNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["UnknownNormal"] = imageUrl
                # Misc
                else:
                    if imageUrl not in datum[id]["Sprites"]["Misc"]:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

    return datum


def main():
    data = {}
    for generation in SPRITE_PAGES:
        sprite_page_url = SPRITE_PAGES[generation]
        print('\nProcessing sprites for Pokemon Generation %s...' % generation)

        html = get_html(sprite_page_url)
        data.update(parse_html(generation, html))

    with open("ImprovedSpriteList.json", "w") as outfile:
        json.dump(data, outfile)
    print('\nDone!')


if __name__ == "__main__":
    # main()
    data = {}
    data.update(parse_Json())

    with open("FromOldJson.json", "w") as outfile:
        json.dump(data, outfile)
