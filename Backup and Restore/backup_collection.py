import sys
import json
from pathlib import Path
from datetime import datetime
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection
from Utilities.helpers import ensure_directory

def backup_collection(db_name, collection_name, backup_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ensure_directory(backup_dir)
    
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    documents = list(collection.find())
    
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    
    output_file = Path(backup_dir) / f"{collection_name}_{timestamp}.json"
    with open(output_file, 'w') as f:
        json.dump(documents, f, indent=2)
    
    client.close()
    print(f"✓ Backed up {len(documents)} documents to {output_file}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    backup_dir = input("Backup directory: ").strip()
    backup_collection(db_name, collection_name, backup_dir)
