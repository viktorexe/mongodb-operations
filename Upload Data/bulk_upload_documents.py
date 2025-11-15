import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def bulk_upload_documents(db_name, collection_name, documents):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    
    result = collection.insert_many(documents)
    client.close()
    print(f"✓ Uploaded {len(result.inserted_ids)} documents")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    json_data = input("Enter JSON array of documents: ").strip()
    documents = json.loads(json_data)
    bulk_upload_documents(db_name, collection_name, documents)
