import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database

def list_collections(db_name):
    client = get_mongo_client()
    db = get_database(client, db_name)
    collections = db.list_collection_names()
    print(f"\nCollections in '{db_name}':")
    for coll in collections:
        print(f"  - {coll}")
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    list_collections(db_name)
