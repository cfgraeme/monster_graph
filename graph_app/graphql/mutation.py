import strawberry

from ..db.models import Monster, Movie
from .schema import MonsterSchema, MovieSchema

from typing import Optional


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_movie(
        self, info, title: str, year: int, synopsis: str, director: str
    ) -> MovieSchema:
        db = info.context["db"]
        new_movie = Movie(
            title=title,
            year=year,
            synopsis=synopsis,
            director=director,
        )
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie

    @strawberry.mutation
    def add_monster(
        self, info, name: str, classification: str, movies: Optional[list[str]] = None
    ) -> MonsterSchema:
        db = info.context["db"]
        new_monster = Monster(name=name, classification=classification)
        if movies:
            for movie in movies:
                movie = db.query(Movie).filter(Movie.title == movie).first()
                if movie:
                    new_monster.movies.append(movie)
        db.add(new_monster)
        db.commit()
        db.refresh(new_monster)
        return new_monster
