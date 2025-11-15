import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def insert_document(db_name, collection_name, document):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    result = collection.insert_one(document)
    client.close()
    print(f"✓ Document inserted with ID: {result.inserted_id}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    doc_json = input("Document (JSON): ").strip()
    document = json.loads(doc_json)
    insert_document(db_name, collection_name, document)
