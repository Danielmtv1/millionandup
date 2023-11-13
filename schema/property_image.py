def individual_Serial(todo) -> dict:
    return {
        "id_property": todo['id_property'],
        "file": todo['file'],
        "enabled": todo['enabled']
    }


def list_property_image(todos) -> list:
    return [individual_Serial(todo) for todo in todos]
