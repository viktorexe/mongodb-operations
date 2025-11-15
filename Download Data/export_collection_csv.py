import sys
import csv
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def export_collection_to_csv(db_name, collection_name, output_file):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    
    documents = list(collection.find())
    if not documents:
        print("No documents found")
        return
    
    keys = set()
    for doc in documents:
        keys.update(doc.keys())
    
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sorted(keys))
        writer.writeheader()
        for doc in documents:
            doc['_id'] = str(doc['_id'])
            writer.writerow(doc)
    
    client.close()
    print(f"✓ Exported {len(documents)} documents to {output_file}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    output_file = input("Output file path: ").strip()
    export_collection_to_csv(db_name, collection_name, output_file)
