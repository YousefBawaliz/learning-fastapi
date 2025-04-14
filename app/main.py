import select
import sys
from typing import Annotated
from fastapi import FastAPI, Response, status, HTTPException, Query
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from sqlmodel import select
import time
from .models import Post
from .database import SessionDep, create_db_and_tables



app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

    
@app.get("/")
async def root():
    return {"message": "Hello Mee"}

@app.get("/posts")
def get_all_posts(
    session: SessionDep,
) -> list[Post]:
    posts = session.exec(select(Post)).all()   
    return posts 
    
    

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(newPost: Post):
    pass


@app.get("/posts/{id}") # path parameters are always considered strings.
def get_single_post(id: int, response: Response): # specify id as int
    pass

@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    pass


@app.put("/posts/{id}")
def update_post(id: int, post: Post, response: Response):
    pass