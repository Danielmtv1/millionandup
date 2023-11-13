
def individual_Serial(todo) -> dict:
    print(todo)
    return {
        "id": str(todo['_id']),
        "name": todo['name'],
        "address": todo['address'],
        "price": todo['price'],
        "year": todo['year'],
        "id_owner": todo['id_owner']
    }


def list_property(todos) -> list:
    return [individual_Serial(todo) for todo in todos]
