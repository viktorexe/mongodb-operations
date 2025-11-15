import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def list_indexes(db_name, collection_name):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    indexes = list(collection.list_indexes())
    
    print(f"\nIndexes in '{collection_name}':")
    for idx in indexes:
        print(f"  - {idx['name']}: {idx['key']}")
    
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    list_indexes(db_name, collection_name)
