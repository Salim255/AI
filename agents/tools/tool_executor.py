def get_user(user_id: int):
    # Replace this with your real DB later
    fake_db = {
        1: {"id": 1, "name": "Alice", "age": 30},
        2: {"id": 2, "name": "Bob", "age": 25},
        7: {"id": 7, "name": "Sarah", "age": 29},
    }
    return fake_db.get(user_id, {"error": "User not found"})
