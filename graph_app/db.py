from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from strawberry.extensions import Extension

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class SQLAlchemySession(Extension):
    def on_request_start(self):
        self.execution_context.context["db"] = SessionLocal()

    def on_request_end(self):
        self.execution_context.context["db"].close()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
