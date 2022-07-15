from typing import Optional, BinaryIO

from firebase_admin import storage


def upload_public_file(file: Optional[BinaryIO], filename: str, content_type: Optional[str]):
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_file(file_obj=file, content_type=content_type)
    blob.make_public()
    return blob.public_url
