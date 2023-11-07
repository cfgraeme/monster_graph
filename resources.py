from typing import List

import strawberry

from data import movies_data


@strawberry.type
class Monster:
    name: str
    type: str
    movies: List["Movie"]


@strawberry.type
class Movie:
    id: int
    title: str
    year: int
    synopsis: str


def movie_from_id(movie_id: int) -> Movie:
    movie_info = movies_data[movie_id]
    return Movie(
        id=movie_id,
        title=movie_info["title"],
        year=movie_info["year"],
        synopsis=movie_info["synopsis"],
    )

