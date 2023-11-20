# pylint: disable=W0622

from typing import Optional

from .models import Monster, Movie


def get_all_movies(info, before: int = None, after: int = None, director: str = None):
    query = info.context["db"].query(Movie)

    if before is not None:
        query = query.filter(Movie.year < before)

    if after is not None:
        query = query.filter(Movie.year > after)

    if director is not None:
        query = query.filter(Movie.director == director)

    return query.all()


def get_all_monsters(info, classification: str = None):
    query = info.context["db"].query(Monster)

    if classification is not None:
        query = query.filter(Monster.classification == classification)

    return query.all()


def get_monster(info, id: Optional[int] = None, name: Optional[str] = None):
    query = info.context["db"].query(Monster)

    if id is not None:
        query = query.filter(Monster.id == id)
    elif name is not None:
        query = query.filter(Monster.name == name)

    return query.first()


def get_movie(info, id: Optional[int] = None, title: Optional[str] = None):
    query = info.context["db"].query(Movie)

    if id is not None:
        query = query.filter(Movie.id == id)
    elif title is not None:
        query = query.filter(Movie.title == title)

    return query.first()
