# pylint: disable=W0622

from typing import Optional

from ..db.models import Monster, Movie


def get_all_movies(
    info,
    title: Optional[str] = None,
    before: Optional[int] = None,
    after: Optional[int] = None,
    director: Optional[str] = None,
):
    query = info.context["db"].query(Movie)

    if title is not None:
        query = query.filter(Movie.title == title)

    if before is not None:
        query = query.filter(Movie.year < before)

    if after is not None:
        query = query.filter(Movie.year > after)

    if director is not None:
        query = query.filter(Movie.director == director)

    return query.all()


def get_all_monsters(
    info, name: Optional[str] = None, classification: Optional[str] = None
):
    query = info.context["db"].query(Monster)

    if name is not None:
        query = query.filter(Monster.name == name)

    if classification is not None:
        query = query.filter(Monster.classification == classification)

    return query.all()


def get_monster(info, id: Optional[int] = None):
    query = info.context["db"].query(Monster)

    if id is not None:
        query = query.filter(Monster.id == id)

    return query.first()


def get_movie(info, id: Optional[int] = None):
    query = info.context["db"].query(Movie)

    if id is not None:
        query = query.filter(Movie.id == id)

    return query.first()
