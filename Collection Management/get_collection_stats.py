import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database

def get_collection_stats(db_name, collection_name):
    client = get_mongo_client()
    db = get_database(client, db_name)
    stats = db.command("collStats", collection_name)
    
    print(f"\nCollection: {collection_name}")
    print(f"Document Count: {stats['count']}")
    print(f"Size: {stats['size'] / (1024**2):.2f} MB")
    print(f"Storage Size: {stats['storageSize'] / (1024**2):.2f} MB")
    print(f"Indexes: {stats['nindexes']}")
    print(f"Total Index Size: {stats['totalIndexSize'] / (1024**2):.2f} MB")
    
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    get_collection_stats(db_name, collection_name)
