import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_database
from Utilities.helpers import ensure_directory

def download_database(db_name, output_dir):
    client = get_mongo_client()
    db = get_database(client, db_name)
    
    ensure_directory(output_dir)
    collections = db.list_collection_names()
    
    for coll_name in collections:
        collection = db[coll_name]
        documents = list(collection.find())
        
        for doc in documents:
            doc['_id'] = str(doc['_id'])
        
        output_file = Path(output_dir) / f"{coll_name}.json"
        with open(output_file, 'w') as f:
            json.dump(documents, f, indent=2)
        
        print(f"✓ Exported {coll_name}: {len(documents)} documents")
    
    client.close()
    print(f"\n✓ Database '{db_name}' downloaded to {output_dir}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    output_dir = input("Output directory: ").strip()
    download_database(db_name, output_dir)
