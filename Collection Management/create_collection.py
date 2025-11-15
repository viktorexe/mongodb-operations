import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database

def create_collection(db_name, collection_name):
    client = get_mongo_client()
    db = get_database(client, db_name)
    db.create_collection(collection_name)
    client.close()
    print(f"✓ Collection '{collection_name}' created in '{db_name}'")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    create_collection(db_name, collection_name)
