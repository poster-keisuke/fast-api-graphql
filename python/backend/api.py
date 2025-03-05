from fastapi import APIRouter

from backend.auth.view import user_router
from backend.post.view import post_router

api_router = APIRouter()


api_router.include_router(user_router, prefix="/users")
api_router.include_router(post_router, prefix="/posts")
