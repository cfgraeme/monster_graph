# Define a dictionary for movies
movies_data = {
    1: {
        "title": "Godzilla (1954)",
        "year": 1954,
        "synopsis": "A giant radioactive lizard terrorizes Tokyo.",
    },
    2: {
        "title": "Godzilla vs. Kong (2021)",
        "year": 2021,
        "synopsis": "Epic battle between monsters.",
    },
    3: {
        "title": "Shin Godzilla (2016)",
        "year": 2016,
        "synopsis": "A new version of Godzilla emerges.",
    },
    4: {
        "title": "King Kong (1933)",
        "year": 1933,
        "synopsis": "A giant ape in the jungle.",
    },
    5: {
        "title": "Kong: Skull Island (2017)",
        "year": 2017,
        "synopsis": "Explorers encounter Kong on an island.",
    },
    6: {
        "title": "Frankenstein (1931)",
        "year": 1931,
        "synopsis": "Mad scientist creates a monster.",
    },
    7: {
        "title": "Bride of Frankenstein (1935)",
        "year": 1935,
        "synopsis": "The monster gets a bride.",
    },
    8: {
        "title": "Young Frankenstein (1974)",
        "year": 1974,
        "synopsis": "Comedy homage to classic horror.",
    },
    9: {
        "title": "Nosferatu (1922)",
        "year": 1922,
        "synopsis": "An early vampire film.",
    },
    10: {
        "title": "Alien (1979)",
        "year": 1979,
        "synopsis": "Terrifying alien in space.",
    },
    11: {
        "title": "Aliens (1986)",
        "year": 1986,
        "synopsis": "Marines face off against aliens.",
    },
    12: {
        "title": "Predator (1987)",
        "year": 1987,
        "synopsis": "An alien hunts soldiers.",
    },
    13: {
        "title": "Predator 2 (1990)",
        "year": 1990,
        "synopsis": "Predator in an urban jungle.",
    },
    14: {
        "title": "Alien 3 (1992)",
        "year": 1992,
        "synopsis": "Ripley faces off against more aliens.",
    },
    15: {
        "title": "Alien: Resurrection (1997)",
        "year": 1997,
        "synopsis": "Cloned Ripley and more alien horrors.",
    },
    16: {
        "title": "Alien vs. Predator (2004)",
        "year": 2004,
        "synopsis": "Aliens and Predators clash in an Antarctic pyramid.",
    },
    17: {
        "title": "Aliens vs. Predator: Requiem (2007)",
        "year": 2007,
        "synopsis": "Alien and Predator battles continue on Earth.",
    },
    18: {
        "title": "Dracula (1931)",
        "year": 1931,
        "synopsis": "Classic vampire tale.",
    },
    19: {
        "title": "Bram Stoker's Dracula (1992)",
        "year": 1992,
        "synopsis": "A more faithful adaptation.",
    },
}

monsters_data = {
    "Godzilla": {
        "type": "Kaiju",
        "movies": [1, 2, 3],
    },
    "King Kong": {
        "type": "Giant Ape",
        "movies": [4, 5],
    },
    "Frankenstein's Monster": {
        "type": "Undead",
        "movies": [6, 7, 8],
    },
    "Nosferatu": {
        "type": "Vampire",
        "movies": [9],
    },
    "Dracula": {
        "type": "Vampire",
        "movies": [18, 19],
    },
    "Xenomorph": {
        "type": "Alien",
        "movies": [10, 11, 14, 15, 16, 17],
    },
    "Predator": {
        "type": "Alien",
        "movies": [12, 13, 16, 17],
    },
}
