def get_user(user_id: int):
    # fake DB for now
    users = {
        1: {"id": 1, "name": "Alice"},
        2: {"id": 2, "name": "Bob"},
    }
    return users.get(user_id, None)
