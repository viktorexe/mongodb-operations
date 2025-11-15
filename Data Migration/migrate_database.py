import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database

def migrate_database(source_db_name, target_db_name):
    client = get_mongo_client()
    source_db = get_database(client, source_db_name)
    target_db = get_database(client, target_db_name)
    
    collections = source_db.list_collection_names()
    
    for coll_name in collections:
        source_coll = source_db[coll_name]
        target_coll = target_db[coll_name]
        
        documents = list(source_coll.find())
        if documents:
            target_coll.insert_many(documents)
            print(f"✓ Migrated {coll_name}: {len(documents)} documents")
    
    client.close()
    print(f"\n✓ Database migrated from '{source_db_name}' to '{target_db_name}'")

if __name__ == "__main__":
    source_db = input("Source database: ").strip()
    target_db = input("Target database: ").strip()
    migrate_database(source_db, target_db)
