import os

import nanoid
from fastapi import UploadFile

from app.services import firebase_storage_service


def upload_file(u_file: UploadFile):
    extension = os.path.splitext(u_file.filename)[1]
    filename = f"{nanoid.generate()}{extension}"
    return firebase_storage_service.upload_public_file(file=u_file.file,
                                                       content_type=u_file.content_type,
                                                       filename=filename)
