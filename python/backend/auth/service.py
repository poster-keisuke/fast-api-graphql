def get(user_id: int):
    return {"user_id": user_id, "message": "user get success"}


def create_or_update_user(user_id: int):
    return {"user_id": user_id, "message": "user create success"}
