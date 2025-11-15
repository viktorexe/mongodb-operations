import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def update_documents(db_name, collection_name, query, update):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    result = collection.update_many(query, update)
    client.close()
    print(f"✓ Matched: {result.matched_count}, Modified: {result.modified_count}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    query_json = input("Query (JSON): ").strip()
    update_json = input("Update (JSON with $set, $inc, etc.): ").strip()
    query = json.loads(query_json)
    update = json.loads(update_json)
    update_documents(db_name, collection_name, query, update)
