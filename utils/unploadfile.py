from fastapi import File, UploadFile

from config.database import fs


async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    file_id = await fs.upload_from_stream(
        file.filename, contents, metadata={"Content-Type": file.content_type}
    )

    return {"file_id": str(file_id)}
