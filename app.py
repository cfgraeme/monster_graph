
from fastapi import FastAPI
from query import Query

from strawberry.asgi import GraphQL
from strawberry import Schema

schema = Schema(query=Query)
graphql_app = GraphQL(schema)

app = FastAPI()
app.mount("/graphql", graphql_app)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
