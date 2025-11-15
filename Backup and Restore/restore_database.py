import sys
import json
from pathlib import Path
from bson import ObjectId
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database

def restore_database(db_name, backup_dir):
    client = get_mongo_client()
    db = get_database(client, db_name)
    
    backup_path = Path(backup_dir)
    json_files = list(backup_path.glob("*.json"))
    
    for json_file in json_files:
        collection_name = json_file.stem
        
        with open(json_file, 'r') as f:
            documents = json.load(f)
        
        for doc in documents:
            if '_id' in doc and isinstance(doc['_id'], str):
                try:
                    doc['_id'] = ObjectId(doc['_id'])
                except:
                    pass
        
        if documents:
            db[collection_name].insert_many(documents)
            print(f"✓ Restored {collection_name}: {len(documents)} documents")
    
    client.close()
    print(f"\n✓ Database '{db_name}' restored from {backup_dir}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    backup_dir = input("Backup directory: ").strip()
    restore_database(db_name, backup_dir)
