from fastapi import APIRouter

post_router = APIRouter()


@post_router.get("/{post_id}")
def get_post(post_id: int):
    return {"post_id": post_id}
