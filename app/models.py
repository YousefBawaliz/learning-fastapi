from sqlmodel import SQLModel, Field
from typing import Optional

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str
    published: bool = Field(sa_column_kwargs={"server_default": "true"}, default=True)
    rating: Optional[int] | None = Field(default=None) # means this is nullable 

"""
 default: Only works at the Python/SQLModel level
 server_default: Works at the database level
"""