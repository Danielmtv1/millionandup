def individual_Serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "address": todo["address"],
        "photo": todo["photo"],
        "birthday": todo["birthday"],
    }


def list_owner(todos) -> list:
    return [individual_Serial(todo) for todo in todos]
