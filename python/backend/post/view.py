from fastapi import APIRouter, Depends

from backend.auth.view import AuthClientInterface, get_auth_client

post_router = APIRouter()


class PostClient:
    def get_post_by_id(self, post_id: str):
        return {"post_id": post_id}


def get_post_client() -> PostClient:
    return PostClient()


@post_router.get("/{post_id}")
def get_post(post_id: str, auth_client: AuthClientInterface = Depends(get_auth_client)):
    client = get_post_client()
    user = auth_client.get_user_by_id("user_id")
    post = client.get_post_by_id(post_id)

    return {"post": post, "user": user}
