# Pokemon-Sprite-Scraper

Scrap links to all the Pokémon sprite from https://projectpokemon.org/ and store it in JSON file.

## Run Locally

To generate the "sprites.json" file, just run the python program from wherever you usually do.

## JSON structure

    "0003": {
        "Name": "venusaur",
        "Sprites": {
            "Misc": [
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_fd_n_00000000_f_n.png",
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_fd_n_00000000_f_r.png",
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_md_n_00000000_f_n.png",
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_md_n_00000000_f_r.png",
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_mf_g_00000000_f_n.png",
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_mf_g_00000000_f_r.png",
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_001_mf_n_00000000_f_n.png",
                "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_001_mf_n_00000000_f_r.png"
            ],
            "NormalFemale": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_fd_n_00000000_f_n.png",
            "ShinyFemale": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_fd_n_00000000_f_r.png",
            "NormalMale": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_md_n_00000000_f_n.png",
            "ShinyMale": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_md_n_00000000_f_r.png",
            "GigaNormal": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_mf_g_00000000_f_n.png",
            "NoGenNormal": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_mf_g_00000000_f_n.png",
            "GigaShiny": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_mf_g_00000000_f_r.png",
            "NoGenShiny": "https://projectpokemon.org/images/sprites-models/homeimg/poke_capture_0003_000_mf_g_00000000_f_r.png"
        }
    },

### Note

Partially adapted from https://github.com/yaylinda/pokemon-sprite-scraper
