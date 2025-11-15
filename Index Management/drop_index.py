import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def drop_index(db_name, collection_name, index_name):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    collection.drop_index(index_name)
    client.close()
    print(f"✓ Index '{index_name}' dropped")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    index_name = input("Index name: ").strip()
    drop_index(db_name, collection_name, index_name)
