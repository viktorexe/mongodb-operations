import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database

def get_database_stats(db_name):
    client = get_mongo_client()
    db = get_database(client, db_name)
    stats = db.command("dbStats")
    
    print(f"\nDatabase: {db_name}")
    print(f"Collections: {stats['collections']}")
    print(f"Data Size: {stats['dataSize'] / (1024**2):.2f} MB")
    print(f"Storage Size: {stats['storageSize'] / (1024**2):.2f} MB")
    print(f"Indexes: {stats['indexes']}")
    print(f"Index Size: {stats['indexSize'] / (1024**2):.2f} MB")
    
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    get_database_stats(db_name)
