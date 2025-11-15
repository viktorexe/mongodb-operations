import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def create_index(db_name, collection_name, field, unique=False):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    result = collection.create_index([(field, 1)], unique=unique)
    client.close()
    print(f"✓ Index created: {result}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    field = input("Field name: ").strip()
    unique = input("Unique index? (yes/no): ").strip().lower() == 'yes'
    create_index(db_name, collection_name, field, unique)
