import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def export_collection_to_json(db_name, collection_name, output_file):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    
    documents = list(collection.find())
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    
    with open(output_file, 'w') as f:
        json.dump(documents, f, indent=2)
    
    client.close()
    print(f"✓ Exported {len(documents)} documents to {output_file}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    output_file = input("Output file path: ").strip()
    export_collection_to_json(db_name, collection_name, output_file)
