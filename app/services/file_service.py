from fastapi import UploadFile
from firebase_admin import storage
import nanoid
import os


def upload_file(u_file: UploadFile):
    extension = os.path.splitext(u_file.filename)[1]
    filename = f"{nanoid.generate()}{extension}"
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_file(u_file.file)
    blob.make_public()
    return blob.public_url

