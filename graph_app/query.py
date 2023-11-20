import strawberry

from .resolvers import get_all_monsters, get_all_movies, get_monster, get_movie
from .schema import MonsterSchema, MovieSchema


@strawberry.type
class Query:
    monsters: list[MonsterSchema] = strawberry.field(resolver=get_all_monsters)
    getMonster: MonsterSchema = strawberry.field(resolver=get_monster)
    movies: list[MovieSchema] = strawberry.field(resolver=get_all_movies)
    getMovie: MovieSchema = strawberry.field(resolver=get_movie)
