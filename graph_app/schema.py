import strawberry


@strawberry.type
class MovieSchema:
    id: int
    title: str
    director: str
    year: int
    synopsis: str


@strawberry.type
class MonsterSchema:
    id: int
    name: str
    classification: str
    movies: list[MovieSchema]
