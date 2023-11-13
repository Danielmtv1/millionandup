from fastapi import APIRouter, HTTPException, status
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
    # Create
    @router.post(
            '/',
            response_model=model,
            status_code=status.HTTP_201_CREATED
    )
    async def create_item(item: model):
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
        items_cursor = await collection.find().to_list(None)
        items_serialized = list_serial(items_cursor)
        return items_serialized

    #GET by id
    @router.get('/{item_id}')
    async def read_item(item_id: str):
        item = await collection.find_one({"_id": ObjectId(item_id)})
        print(item)
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")

        item_serialized = serializer(item)
        return item_serialized
    # Update
    @router.put('/{item_id}')
    async def update_item(item_id: str, updated_item: model):
        item_dict = updated_item.model_dump()
        await collection.find_one_and_update(
            {"_id": ObjectId(item_id)},
            {"$set": dict(item_dict)}
        )
        return updated_item

    # Delete
    @router.delete('/{item_id}')
    async def delete_item(item_id: str):
        collection.find_one_and_delete({"_id": ObjectId(item_id)})
        return HTTPException(status_code=200, detail="delete ")
