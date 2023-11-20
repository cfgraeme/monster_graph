import json

from .models import Monster, Movie


def reset_data(db, path):
    db.query(Movie).delete()
    db.query(Monster).delete()
    db.commit()
    with open(path, "r") as json_file:
        data = json.load(json_file)

        # Import Monsters
        for monster_data in data.get("monsters", []):
            print(monster_data)
            monster = Monster(**monster_data)
            db.add(monster)
        db.commit()

        # Import Movies
        for movie_data in data.get("movies", []):
            print(movie_data)
            monster_ids = movie_data.pop("monsters", [])
            movie = Movie(**movie_data)

            # Associate Monsters with Movies
            for monster_id in monster_ids:
                monster = db.query(Monster).filter(Monster.id == monster_id).first()
                if monster:
                    movie.monsters.append(monster)
            db.add(movie)

        db.commit()
        db.close()
