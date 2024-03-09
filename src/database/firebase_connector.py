# firebase_connector.py

from google.cloud import firestore
import json

credentials_path = './firebase_credentials.json'
with open(credentials_path)as json_file:
    credentials_info = json.load(json_file)

db = firestore.Client.from_service_account_info(credentials_info)