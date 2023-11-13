def individual_Serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "data_sale": todo["data_sale"],
        "name": todo["name"],
        "value": todo["value"],
        "tax": todo["tax"],
        "id_property": todo["id_property"],
    }


def list_property_trace(todos) -> list:
    return [individual_Serial(todo) for todo in todos]
