from fastapi import APIRouter, HTTPException, status, Query
from typing import Type, Callable
from pymongo.collection import Collection
from pydantic import BaseModel
from bson import ObjectId


def create_generic_routes(
        router: APIRouter,
        model: Type[BaseModel],
        collection: Collection,
        list_serial: Callable,
        serializer: Callable
):
    """
    Create generic CRUD routes for a FastAPI application.

    :param router: The FastAPI router to which the routes will be added.
    :param model: The Pydantic model representing the data structure.
    :param collection: The MongoDB collection associated with the model.
    :param list_serial: The serialization function for listing items.
    :param serializer: The serialization function for individual items.
    """
    # Create
    @router.post(
            '/',
            response_model=model,
            status_code=status.HTTP_201_CREATED
    )
    async def create_item(item: model):
        """
        Create a new item.

        :param item: The data for the new item.

        :return: The created item.
        """
        try:
            item_dict = item.model_dump()
            inserted_result = await collection.insert_one(item_dict)
            inserted_item = await collection.find_one(
                {"_id": inserted_result.inserted_id}
            )
            return inserted_item
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Internal Server Error: {str(e)}")

    # Read (Get All)
    @router.get('/')
    async def read_all_items():
        """
        Get all items.

        :return: List of all items.
        """
        items_cursor = await collection.find().to_list(None)
        items_serialized = list_serial(items_cursor)
        return items_serialized

    # GET by id
    @router.get('/{item_id}')
    async def read_item(item_id: str):
        """
        Get an item by its ID.

        :param item_id: The ID of the item to retrieve.

        :return: The requested item.
        """
        item = await collection.find_one({"_id": ObjectId(item_id)})
        print(item)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")

        item_serialized = serializer(item)
        return item_serialized

    # Update
    @router.put('/{item_id}')
    async def update_item(item_id: str, updated_item: model):
        """
        Update an existing item.

        :param item_id: The ID of the item to update.
        :param updated_item: The updated data for the item.

        :return: The updated item.
        """
        item_dict = updated_item.model_dump()
        await collection.find_one_and_update(
            {"_id": ObjectId(item_id)},
            {"$set": dict(item_dict)}
        )
        return updated_item

    # Delete
    @router.delete('/{item_id}')
    async def delete_item(item_id: str):
        """
        Delete an item by its ID.

        :param item_id: The ID of the item to delete.

        :return: HTTP response indicating the success of the deletion.
        """
        collection.find_one_and_delete({"_id": ObjectId(item_id)})
        return HTTPException(status_code=200, detail="delete ")

    # search
    @router.post('/search', response_model=list[model])
    async def search_items(
        query_params: model,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, le=100)
    ):
        """
        Search for items based on specific criteria.

        :param query_params: The search parameters.
        :param skip: Number of items to skip in the result (default: 0).
        :param limit: Maximum number of items to return (default: 10, max: 100).

        :return: List of items that match the search criteria.
        """
        non_null_fields = {key: value for key, value in query_params.model_dump().items() if value is not None} # noqa
        if len(non_null_fields) == 1:
            field_name, field_value = non_null_fields.popitem()
            query_dict = {field_name: field_value}
        else:
            raise HTTPException(
                status_code=400,
                detail="Exactly one non-null field is required for search."
            )

        items_cursor = await (
            collection
            .find(query_dict)
            .skip(skip)
            .limit(limit).to_list(None))
        items_serialized = list_serial(items_cursor)
        return items_serialized
