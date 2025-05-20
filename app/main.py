from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from db.posts import get_posts
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/post")
async def list_post():
    posts = get_posts()
    return posts