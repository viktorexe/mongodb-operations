import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def count_documents(db_name, collection_name, query):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    count = collection.count_documents(query)
    client.close()
    print(f"✓ Document count: {count}")

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    query_json = input("Query (JSON, empty for all): ").strip()
    query = json.loads(query_json) if query_json else {}
    count_documents(db_name, collection_name, query)
