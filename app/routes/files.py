from fastapi import APIRouter, UploadFile, File
import hashlib
import os

router = APIRouter()

CHUNK_SIZE = 4 * 1024 * 1024  # 4MB

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Uploads a file and splits it into chunks"""
    file_id = hashlib.sha256(file.filename.encode()).hexdigest()
    storage_path = f"storage/node_1/{file_id}"
    
    with open(storage_path, "wb") as buffer:
        buffer.write(await file.read())

    return {"message": f"File {file.filename} uploaded successfully!", "file_id": file_id}
