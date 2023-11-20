import os

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from .mutation import Mutation
from .query import Query

from .data_import import reset_data
from .db import SQLAlchemySession, engine, get_db
from .models import Base

Base.metadata.create_all(bind=engine)

cwd = os.getcwd()
filename = cwd + "/graph_app/sample.json"
reset_data(next(get_db()), filename)


schema = strawberry.Schema(
    query=Query, mutation=Mutation, extensions=[SQLAlchemySession]
)

graphql_app = GraphQL(schema)


app = FastAPI()

app.add_route("/graphql", graphql_app)
