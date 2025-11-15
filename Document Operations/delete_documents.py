import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def delete_documents(db_name, collection_name, query):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    confirm = input(f"Delete documents matching query? (yes/no): ").strip().lower()
    if confirm == 'yes':
        result = collection.delete_many(query)
        print(f"✓ Deleted {result.deleted_count} documents")
    else:
        print("Operation cancelled")
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    query_json = input("Query (JSON): ").strip()
    query = json.loads(query_json)
    delete_documents(db_name, collection_name, query)
