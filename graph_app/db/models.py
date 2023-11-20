# models.py
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

monster_movie_association = Table(
    "monster_movie_association",
    Base.metadata,
    Column("monster_id", Integer, ForeignKey("monsters.id")),
    Column("movie_id", Integer, ForeignKey("movies.id")),
)


class Monster(Base):
    __tablename__ = "monsters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    classification = Column(String)

    movies = relationship(
        "Movie", secondary=monster_movie_association, back_populates="monsters"
    )


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    synopsis = Column(String)
    director = Column(String)

    monsters = relationship(
        "Monster", secondary=monster_movie_association, back_populates="movies"
    )
