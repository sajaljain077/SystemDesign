from ast import While
from fastapi import Depends, FastAPI, status, Response, HTTPException
from matplotlib.pyplot import title
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from app.database import engine, get_db 
from app import models
from pydantic import BaseModel
from app.models import Posts

models.Base.metadata.create_all(bind=engine)

app= FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True

@app.get("/")
async def root():
    return {"message":"This is my first personal web project"}


@app.get('/sqlalchemy')
async def get_post(db:Session = Depends(get_db)):
    all_posts = db.query(Posts).all()
    return {"data":all_posts}

# @app.get("/posts", )
# async def getPosts():
#     cursor.execute("SELECT * FROM posts order by id")
#     posts = cursor.fetchall()
#     return {'data': posts}

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# async def createPosts(post:Post):
#     cursor.execute("""INSERT INTO posts (title, content, published) values (%s, %s, %s) RETURNING * """, 
#     (post.title, post.content, post.published))
#     newPost = cursor.fetchone()
#     conn.commit()
#     return {'data':newPost}

# @app.get('/posts/{id}', status_code=status.HTTP_200_OK)
# async def getOnePost(id:int):
#     cursor.execute("""SELECT * FROM Posts WHERE id = (%s)""", str(id))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id : {id} was not found")
#     return {'data': post}
