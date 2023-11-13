from config.database import (
    collection_owner,
    collection_property,
    collection_property_image,
    collection_property_trace,
    fs
)
import io
from fastapi import APIRouter, HTTPException, status, UploadFile, File
from fastapi.responses import StreamingResponse
from models.owner import Owner
from models.property import Property, Property_price
from models.propertyimage import PropertyImage
from models.propertytrace import PropertyTrace
from schema.owner import list_owner, individual_Serial as serial_owner
from schema.property import list_property, individual_Serial as serial_property
from schema.property_image import list_property_image, individual_Serial as serial_property_image
from schema.property_trace import list_property_trace, individual_Serial as serial_property_trace
from bson import ObjectId
from routes import create_generic_routes
from gridfs.errors import NoFile
from config.database import db
# Property routes
router_property = APIRouter(prefix="/property", tags=["Property"])
create_generic_routes(
    router_property,
    Property,
    collection_property,
    list_property,
    serial_property
)


@router_property.put('price/{item_id}')
async def update_only_price(item_id: str, updated_item: Property_price):
    item_dict = updated_item.model_dump(exclude_unset=True)
    print(item_dict)
    if "price" not in item_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El campo 'price' es requerido para la actualización")

    collection_property.find_one_and_update(
        {"_id": ObjectId(item_id)},
        {"$set": {"price": item_dict["price"]}}
    )

    return updated_item
# Owner routes
router_owner = APIRouter(prefix="/owner", tags=["Owner"])
create_generic_routes(router_owner, Owner, collection_owner, list_owner, serial_owner)

# PropertyTrace routes
router_property_trace = APIRouter(
    prefix="/property_trace",
    tags=["Property Trace"]
)
create_generic_routes(
    router_property_trace,
    PropertyTrace,
    collection_property_trace,
    list_property_trace,
    serial_property_trace
)

# PropertyImage routes
router_property_image = APIRouter(
    prefix="/property_image",
    tags=["Property Image"]
)
# @router_property_image.post(
#             '/property_images',
#             response_model=PropertyImage,
#             status_code=status.HTTP_201_CREATED
#     )
# async def create_item(item: PropertyImage):
#     try:
#         item_dict = item.model_dump()
#         inserted_result = await collection_property_image.insert_one(item_dict)
#         inserted_item = await collection_property_image.find_one(
#             {"_id": inserted_result.inserted_id}
#         )
#         return inserted_item
#     except Exception as e:
#         raise HTTPException(
#             status_code=500, detail=f"Internal Server Error: {str(e)}")


@router_property_image.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):

    contents = await file.read()

    file_id = await fs.upload_from_stream(
        file.filename,
        contents,
        metadata={"Content-Type": file.content_type}
    )

    return {"file_id": str(file_id)}


@router_property_image.get("/file/{file_id}")
async def read_file(file_id: str):
    try:
        object_id = ObjectId(file_id)
        stream = await fs.open_download_stream(object_id)
        file_content = await stream.read()
        return StreamingResponse(io.BytesIO(file_content), media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={file_id}"})
    except NoFile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="File not found",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

router = APIRouter()

router.include_router(router_owner)
router.include_router(router_property)
router.include_router(router_property_trace)
router.include_router(router_property_image)
