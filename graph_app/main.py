import os

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from .db.connect import SQLAlchemySession, engine, get_db
from .db.data_import import reset_data
from .db.models import Base
from .graphql.mutation import Mutation
from .graphql.query import Query

Base.metadata.create_all(bind=engine)

cwd = os.getcwd()
filename = cwd + "/graph_app/db/sample.json"
reset_data(next(get_db()), filename)


schema = strawberry.Schema(
    query=Query, mutation=Mutation, extensions=[SQLAlchemySession]
)

graphql_app = GraphQL(schema)


app = FastAPI()

app.add_route("/graphql", graphql_app)
