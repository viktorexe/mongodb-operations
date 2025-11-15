import sys
import json
from pathlib import Path
from datetime import datetime
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database
from Utilities.helpers import ensure_directory

def backup_database(db_name, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = Path(backup_dir) / f"{db_name}_{timestamp}"
    ensure_directory(backup_path)
    
    client = get_mongo_client()
    db = get_database(client, db_name)
    collections = db.list_collection_names()
    
    for coll_name in collections:
        collection = db[coll_name]
        documents = list(collection.find())
        
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        
        output_file = backup_path / f"{coll_name}.json"
        with open(output_file, 'w') as f:
            json.dump(documents, f, indent=2)
        
        print(f"✓ Backed up {coll_name}: {len(documents)} documents")
    
    client.close()
    print(f"\n✓ Backup completed: {backup_path}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    backup_dir = input("Backup directory: ").strip()
    backup_database(db_name, backup_dir)
