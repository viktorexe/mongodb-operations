import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def rename_collection(db_name, old_name, new_name):
    client = get_mongo_client()
    collection = get_collection(client, db_name, old_name)
    collection.rename(new_name)
    client.close()
    print(f"✓ Collection renamed from '{old_name}' to '{new_name}'")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    old_name = input("Current collection name: ").strip()
    new_name = input("New collection name: ").strip()
    rename_collection(db_name, old_name, new_name)
