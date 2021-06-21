# Pokemon-Sprite-Scraper

Extracts links to all the Pokémon sprite from https://projectpokemon.org/ and stores the URL to JSON file.
Extracts other resourses from the following:
 - [Veekun](https://veekun.com/dex)
 - [PokeApi](https://pokeapi.co/)
 - etc...

## Run Locally

Now it generates 9 seperate JSON files.
1) [PokemonNames.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonNames.json)
2) [PokemonStats.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonStats.json)
3) [PokemonTypes.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonTypes.json)
4) [PokemonGenderRatio.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonGenderRatio.json)
5) [PokemonEvolutionChain.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonEvolutionChain.json)
6) [PokemonDimensions.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonDimensions.json)
7) [PokemonDescriptions.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonDescriptions.json)
8) [PokemonClassifiedSprites.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonClassifiedSprites.json)
9) [PokemonAbilities.json](https://github.com/Gastly-dex/PokedexData/blob/main/PokemonAbilities.json)

In addition to these JSON files, This script also generates 3 folders
1) [PokemonCries](https://github.com/Gastly-dex/PokedexData/tree/main/PokemonCries)
2) [PokemonFootprints](https://github.com/Gastly-dex/PokedexData/tree/main/PokemonFootprints)
3) [PokemonSprites](https://github.com/Gastly-dex/PokedexData/tree/main/PokemonSprites)

The Three folders have around ~4400 files of mp3s and PNGs and everything except Pokemon sprites are named with 4 char format with pokemon id.
Eg: 0001...0898

Pokemon sprites uses a different naming convention.

`poke_capture_(speciesID)_(formId)_(gender)_(isgigantamax?)_00000000_f_(shiny?)`

where,
 - Gender takes values
    - md: Male gender difference
    - fd: Femal gender difference
    - mf: No gender difference
    - uk: unknown gender
 - Shiny takes values
    - n: Normal
    - r: Rare/Shiny
 - isgigantamax takes values
    - n: no
    - g: gigantamax



### Note

(Very)Partially adapted from https://github.com/yaylinda/pokemon-sprite-scraper
