# Name            - done
# Description     - done
# Stats           - done
# Types           - done
# Ability         - done
# Sprites : links - done
# Sprites : PNG   - done
# Evolution chain - done
# Cries           - done
# Footprint       - done
# Dimensions      - done
# Gender          - done

import os
import re
import json
import requests
import unidecode

import urllib.request
import concurrent.futures
from multiprocessing import Process

DEBUG = True

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


# Utilities - Start ================================================================

def getHTML(url, isLog=False):
    if(isLog):
        print('tGetting HTML from %s' % url)
    r = requests.get(url)
    return r.text


def forifier(Id):
    while len(str(Id)) < 4:
        Id = "0"+str(Id)
    return Id


def writeToJsonFile(jsonContent, fileName, mode="w"):
    with open(fileName, mode) as file:
        json.dump(jsonContent, file)


def fixDescription():
    with open("PokemonDescriptions.json", "r") as desc:
        descs = json.load(desc)

    for i in list(descs.keys()):
        descs[i] = unidecode.unidecode(descs[i])

    writeToJsonFile(descs, "PokemonDescriptions.json")


def downloadUrl(url, timeout):
    try:
        r = requests.get(url.split('>')[0].replace('"', ""))
        with open(url.split("https://projectpokemon.org/images/sprites-models/homeimg/")[1].split(">")[0].replace('"', ""), "wb") as sprite:
            sprite.write(r.content)
    except Exception as err:
        print(err)


def getSpriteUrls():
    Urls = []
    for generations in SPRITE_PAGES:
        lines = getHTML(SPRITE_PAGES[generations]).splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith('<img') and 'src="https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_' in line:
                imageUrl = line.split('src="')[1].split('"></td>')[0]
                Urls.append(imageUrl)

    return Urls


def spriteURLgetter(html):
    data = []
    datum = {}
    lines = html.splitlines()
    c=0

    for line in lines:
        line = line.strip()
        c+=1
        
        print("Starting - PokemonClassifiedSprites.json Generation: "+str(c))

        if line.startswith('<img') and 'src="https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_' in line:
            imageUrl = line.split('src="')[1].split('"></td>')[0]
            id = forifier(int(imageUrl.split(
                'https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_')[1][0:4]))

            if id in datum.keys():
                # ShinyMale
                if "_md_n" in imageUrl and "_r." in imageUrl:
                    if "ShinyMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # ShinyFemale
                if "_fd_n" in imageUrl and "_r." in imageUrl:
                    if "ShinyFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyFemale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalMale
                if "_md_n" in imageUrl and "_n." in imageUrl:
                    if "NormalMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalFemale
                if "_fd_n" in imageUrl and "_n." in imageUrl:
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
                if "_mf_n" in imageUrl and "_r." in imageUrl:
                    if "NoGenShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenShiny"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NoGenNormal
                if "_mf_n" in imageUrl and "_n." in imageUrl:
                    if "NoGenNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenNormal"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # Misc
                # elif "_md_n" not in imageUrl and "_fd_n" not in imageUrl and "_mf_" not in imageUrl:
                else:
                    datum[id]["Sprites"]["Misc"].append(imageUrl)

                # print(json.dumps(datum[id],sort_keys=True, indent=4))

            else:
                datum[id] = {}
                datum[id]["Sprites"] = {}
                datum[id]["Sprites"]["Misc"] = []
                # ShinyMale
                if "_md_n" in imageUrl and "_r." in imageUrl:
                    if "ShinyMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # ShinyFemale
                if "_fd_n" in imageUrl and "_r." in imageUrl:
                    if "ShinyFemale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["ShinyFemale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalMale
                if "_md_n" in imageUrl and "_n." in imageUrl:
                    if "NormalMale" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NormalMale"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NormalFemale
                if "_fd_n" in imageUrl and "_n." in imageUrl:
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
                if "_mf_n" in imageUrl and "_r." in imageUrl:
                    if "NoGenShiny" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenShiny"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # NoGenNormal
                if "_mf_n" in imageUrl and "_n." in imageUrl:
                    if "NoGenNormal" not in datum[id]["Sprites"].keys():
                        datum[id]["Sprites"]["NoGenNormal"] = imageUrl
                    else:
                        datum[id]["Sprites"]["Misc"].append(imageUrl)

                # Misc
                # elif "_md_n" not in imageUrl and "_fd_n" not in imageUrl and "_mf_" not in imageUrl:
                else:
                    datum[id]["Sprites"]["Misc"].append(imageUrl)

    return datum

# Utilities - End ================================================================


def getPokemonNames():
    apiEndpoint = "https://pokeapi.co/api/v2/pokemon/"
    FinalData = {}

    for id in range(1, 899):
        RetrivedData = json.loads(getHTML(apiEndpoint+str(id)))
        if(DEBUG):
            print("Starting - PokemonName.json Generation: "+str(id), end="\r")

        FinalData[forifier(id)] = RetrivedData["name"]

    writeToJsonFile(FinalData, "PokemonNames.json")
    print("Done - PokemonName.json Generated")


def getDescriptions():

    url = "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/pokedex.json"
    desc = json.loads(getHTML(url))
    FinalData = {}
    pokeid = 0
    for pokemon in desc:
        pokeid += 1
        if(DEBUG):
            print("Starting - PokemonDescriptions.json Generation: " +
                  str(pokeid), end="\r")
        FinalData[forifier(pokeid)] = pokemon["description"]

    writeToJsonFile(FinalData, "PokemonDescriptions.json")
    fixDescription()
    print("Done - PokemonDescriptions.json Generated")


def getStats():
    url = "https://pokeapi.co/api/v2/pokemon/"
    FinalData = {}

    for j in range(1, 899):
        if(DEBUG):
            print("Starting - PokemonStats.json Generation: "+str(j), end="\r")

        stat = json.loads(getHTML(url+str(j)))
        stats = {}
        for i in stat["stats"]:
            if i["stat"]["name"] == "hp":
                stats["HP"] = i["base_stat"]
            elif i["stat"]["name"] == "attack":
                stats["Attack"] = i["base_stat"]
            elif i["stat"]["name"] == "defense":
                stats["Defense"] = i["base_stat"]
            elif i["stat"]["name"] == "special-attack":
                stats["Sp. Attack"] = i["base_stat"]
            elif i["stat"]["name"] == "special-defense":
                stats["Sp. Defense"] = i["base_stat"]
            elif i["stat"]["name"] == "speed":
                stats["Speed"] = i["base_stat"]
        FinalData[forifier(j)] = stats

    writeToJsonFile(FinalData, "PokemonStats.json")
    print("Done - PokemonStats.json Generated")


def getTypes():
    url = "https://pokeapi.co/api/v2/pokemon/"
    FinalData = {}

    for i in range(1, 899):
        if(DEBUG):
            print("Starting - PokemonTypes.json Generation: "+str(i), end="\r")
        types = json.loads(getHTML(url+str(i)))["types"]
        types = [i["type"]["name"].capitalize() for i in types]
        FinalData[forifier(i)] = types

    writeToJsonFile(FinalData, "PokemonTypes.json")
    print("Done - PokemonTypes.json Generated")


def getAbilities():
    url = "https://pokeapi.co/api/v2/pokemon/"
    FinalData = {}

    for i in range(1, 899):
        if(DEBUG):
            print("Starting - PokemonAbilities.json Generation: "+str(i), end="\r")
        abilites = json.loads(getHTML(url+str(i)))["abilities"]
        abilites = [i["ability"]["name"].capitalize() for i in abilites]
        FinalData[forifier(i)] = abilites

    writeToJsonFile(FinalData, "PokemonAbilities.json")
    print("Done - PokemonAbilities.json Generated")


def getEvolution():
    url = "https://pokeapi.co/api/v2/pokemon-species/"
    FinalData = {}

    for i in range(1, 899):
        if(DEBUG):
            print("Starting - PokemonEvolutionChain.json Generation: "+str(i), end="\r")
        evolutionChainUrl = getHTML(
            url+str(i)).split('"evolution_chain":{"url":"')[1].split('"},')[0]
        rawData = getHTML(evolutionChainUrl)
        evolutionChainIds = re.findall(
            r"https://pokeapi.co/api/v2/pokemon-species/([1-9][0-9][0-9]|[1-9][0-9]|[1-9])", rawData)
        FinalData[forifier(i)] = list(map(forifier, evolutionChainIds))

    writeToJsonFile(FinalData, "PokemonEvolutionChain.json")
    print("Done - PokemonEvolutionChain.json Generated")


def getCries():
    if os.path.exists(os.getcwd()+r"\PokemonCries"):
        os.chdir(os.getcwd()+r"\PokemonCries")
        for i in range(1, 899):
            if(DEBUG):
                print("Starting - PokemonCries Generation: "+str(i), end="\r")
            cryUrl = "https://pokemoncries.com/cries/"+str(i)+".mp3"
            try:
                r = requests.get(cryUrl)
                with open(forifier(i)+".mp3", "wb") as cry:
                    cry.write(r.content)
            except:
                pass
        print("Done - PokemonCries Generated with cries .mp3")
    else:
        os.mkdir(os.getcwd()+r"\PokemonCries")
        getCries()


def getFootprints():
    if os.path.exists(os.getcwd()+r"\PokemonFootprints"):
        os.chdir(os.getcwd()+r"\PokemonFootprints")
        for i in range(1, 899):
            if(DEBUG):
                print("Starting - PokemonFootprints Generation: "+str(i), end="\r")
            url = "https://veekun.com/dex/media/pokemon/footprints/" + \
                str(i)+".png"
            try:
                r = requests.get(url)
                with open(forifier(i)+".png", "wb") as feet:
                    feet.write(r.content)
                print("Done - PokemonFootprints Generated with footprints .png")
            except:
                pass
    else:
        os.mkdir(os.getcwd()+r"\PokemonFootprints")
        getFootprints()


def getDimensions():
    url = "https://pokeapi.co/api/v2/pokemon/"
    FinalData = {}
    for id in range(1, 899):
        if(DEBUG):
            print("Starting - PokemonDimensions.json Generation: "+str(id), end="\r")
        Dimensions = {}
        dimes = json.loads(getHTML(url+str(id), False))
        Dimensions["Height"] = str(dict(dimes)["height"]/10)+"m"
        Dimensions["Weight"] = str(dict(dimes)["weight"]/10)+"kg"
        FinalData[forifier(id)] = Dimensions

    writeToJsonFile(FinalData, "PokemonDimensions.json")
    print("Done - PokemonDimensions.json Generated")


def getGenderRatio():
    url = "https://raw.githubusercontent.com/Purukitto/pokemon-data.json/master/pokedex.json"
    genders = json.loads(getHTML(url))
    FinalData = {}
    pokeid = 0

    for pokemon in genders:
        gen = {}
        pokeid += 1
        if(DEBUG):
            print("Starting - PokemonGenderRatio.json Generation: " +
                  str(pokeid), end="\r")

        try:
            genderData = str(pokemon["profile"]["gender"])
            if(genderData != "Genderless"):
                gen["Male"] = float(genderData.split(":")[0])
                gen["Female"] = float(genderData.split(":")[1])
            else:
                gen["Male"] = 0
                gen["Female"] = 0
        except:
            gen["Male"] = 0
            gen["Female"] = 0
        FinalData[forifier(pokeid)] = gen

    writeToJsonFile(FinalData, "PokemonGenderRatio.json")
    print("Done - PokemonGenderRatio.json Generated")


def getClassifiedSpriteUrls():
    FinalData = {}
    for generation in SPRITE_PAGES:
        FinalData.update(spriteURLgetter(getHTML(SPRITE_PAGES[generation])))

    writeToJsonFile(FinalData, "PokemonClassifiedSprites.json")
    print("Done - PokemonClassifiedSprites.json Generated")


def downloadSprites():
    print("Starting - PokemonSprites Generation")
    if os.path.exists(os.getcwd()+r"\PokemonSprites"):
        os.chdir(os.getcwd()+r"\PokemonSprites")
        URLS = getSpriteUrls()
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url = {executor.submit(
                downloadUrl, url, 60): url for url in URLS}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
                else:
                    print('%r page is %d bytes' % (url, len(data)))

    else:
        os.mkdir(os.getcwd()+r"\PokemonSprites")
        downloadSprites()


if __name__ == "__main__":

    Process(target=getStats).start()
    Process(target=getTypes).start()
    Process(target=getAbilities).start()
    Process(target=getEvolution).start()
    Process(target=getDimensions).start()
    Process(target=getPokemonNames).start()


    Process(target=getGenderRatio).start()
    Process(target=getDescriptions).start()
    Process(target=getClassifiedSpriteUrls).start()

    # Network and storage intensive functions. Don't panic if it takes a lot of time.
    # Process(target=getCries).start()
    # Process(target=getFootprints).start()
    # Process(target=downloadSprites).start()
