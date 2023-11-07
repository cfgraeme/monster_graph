from typing import List

import strawberry

from data import monsters_data, movies_data
from resources import Monster, Movie, movie_from_id


@strawberry.type
class Query:
    @strawberry.field
    def monster(self, name: str) -> Monster:
        if name in monsters_data:
            monster_info = monsters_data[name]
            movie_list = [
                movie_from_id(movie_id) for movie_id in monster_info["movies"]
            ]
            return Monster(name=name, type=monster_info["type"], movies=movie_list)
        else:
            return None

    @strawberry.field
    def monsters(
        self,
        type: str = None,
    ) -> List[Monster]:
        if type:
            return [
                Monster(
                    name=monster_name,
                    type=monster_info["type"],
                    movies=[
                        movie_from_id(movie_id) for movie_id in monster_info["movies"]
                    ],
                )
                for monster_name, monster_info in monsters_data.items()
                if monster_info["type"] == type
            ]
        else:
            return [
                Monster(
                    name=monster_name,
                    type=monster_info["type"],
                    movies=[
                        movie_from_id(movie_id) for movie_id in monster_info["movies"]
                    ],
                )
                for monster_name, monster_info in monsters_data.items()
            ]

    @strawberry.field
    def movie(self, title: str) -> Movie:
        for id, movie_info in movies_data:
            if movie_info["title"] == title:
                return Movie(
                    id=id,
                    title=title,
                    year=movie_info["year"],
                    synopsis=movie_info["synopsis"],
                )
        return None

    @strawberry.field
    def movies(self, before: int = None, after: int = None) -> List[Movie]:
        result = [
            Movie(
                id=id,
                title=movie_info["title"],
                year=movie_info["year"],
                synopsis=movie_info["synopsis"],
            )
            for id, movie_info in movies_data.items()
        ]
        if before:
            result = [movie for movie in result if movie.year < before]
        if after:
            result = [movie for movie in result if movie.year > after]
        return result
