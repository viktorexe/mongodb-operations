import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client

def create_database(db_name, collection_name):
    client = get_mongo_client()
    db = client[db_name]
    db[collection_name].insert_one({"_init": True})
    db[collection_name].delete_one({"_init": True})
    client.close()
    print(f"✓ Database '{db_name}' created with collection '{collection_name}'")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Initial collection name: ").strip()
    create_database(db_name, collection_name)
