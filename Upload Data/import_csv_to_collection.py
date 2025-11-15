import sys
import csv
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def import_csv_to_collection(db_name, collection_name, input_file):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        documents = list(reader)
    
    result = collection.insert_many(documents)
    client.close()
    print(f"✓ Imported {len(result.inserted_ids)} documents")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    input_file = input("Input CSV file: ").strip()
    import_csv_to_collection(db_name, collection_name, input_file)
