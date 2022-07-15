from fastapi import UploadFile, APIRouter

from app.services import file_service

router = APIRouter(prefix="/api/v1/files", tags=["Files"])


@router.post("", response_model=str)
def upload_file(file: UploadFile):
    return file_service.upload_file(file)
