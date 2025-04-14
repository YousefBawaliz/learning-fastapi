from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

# Database URL configuration
SQLMODEL_DATABASE_URL = "postgresql://postgres:Ali2k7Ali2k7@localhost:5432/fastapi"

# Create engine
engine = create_engine(SQLMODEL_DATABASE_URL)

# Database initialization function
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)



"""
This is a dependency function that creates a database session using SQLModel (which is built on SQLAlchemy). Here's what each part does:

def get_session(): - Defines a function that will be used as a FastAPI dependency to provide database sessions
with Session(engine) as session: - Creates a new database session using the configured engine:
Session(engine) creates a new session
The with statement ensures the session is properly closed after use
The session is bound to the variable session
yield session - Instead of returning the session, it yields it:
This makes it a generator function
FastAPI will use this session for the duration of a request
After the request is complete, FastAPI will automatically close the session
This ensures proper cleanup of database resources
"""

# Session dependency
def get_session():
    with Session(engine) as session:
        yield session




# Type annotation for dependency injection
SessionDep = Annotated[Session, Depends(get_session)]
