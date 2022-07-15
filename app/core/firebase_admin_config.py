import json
import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials

# Load env
load_dotenv()

# Init firebase admin
service_account_json = os.environ.get("FIREBASE_SERVICE_ACCOUNT_JSON")
bucket_url = os.environ.get('FIREBASE_STORAGE_BUCKET_URL')
service_account = json.loads(service_account_json)
cred = credentials.Certificate(cert=service_account)


def init_firebase():
    try:
        default_app = firebase_admin.initialize_app(cred, {
            'storageBucket': bucket_url,
        })
        print(f"Firebase Admin initialize with project id -> {default_app.project_id}")
    except Exception as err:
        print(f"Cannot init firebase {err}")
