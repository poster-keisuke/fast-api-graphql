from abc import ABC, abstractmethod

from fastapi import APIRouter, Depends

from backend.auth.service import create_or_update_user, get

user_router = APIRouter()


class AuthClientInterface(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass


class AuthClient(AuthClientInterface):
    def get_user_by_id(self, user_id: int):
        user = get(user_id)
        return user


def get_auth_client() -> AuthClientInterface:
    return AuthClient()


@user_router.get("/{user_id}")
def get_user(user_id: int, auth_client: AuthClientInterface = Depends(get_auth_client)):
    return auth_client.get_user_by_id(user_id)


@user_router.post("/")
def create_user(user_id: int):
    return create_or_update_user(user_id)
