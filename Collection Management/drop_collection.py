import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def drop_collection(db_name, collection_name):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    confirm = input(f"Drop '{collection_name}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        collection.drop()
        print(f"✓ Collection '{collection_name}' dropped")
    else:
        print("Operation cancelled")
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    drop_collection(db_name, collection_name)
