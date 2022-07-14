from fastapi import UploadFile
from firebase_admin import storage
import nanoid
import os


def upload_file(u_file: UploadFile):
    extension = os.path.splitext(u_file.filename)[1]
    filename = f"{nanoid.generate()}{extension}"
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_file(file_obj=u_file.file, content_type=u_file.content_type)
    blob.make_public()
    return blob.public_url

