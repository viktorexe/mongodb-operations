import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def find_with_sort(db_name, collection_name, query, sort_field, sort_order, limit=10):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    documents = list(collection.find(query).sort(sort_field, sort_order).limit(limit))
    
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    
    print(json.dumps(documents, indent=2))
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    query_json = input("Query (JSON): ").strip()
    sort_field = input("Sort field: ").strip()
    sort_order = int(input("Sort order (1 for asc, -1 for desc): ").strip())
    query = json.loads(query_json)
    limit = int(input("Limit (default 10): ").strip() or 10)
    find_with_sort(db_name, collection_name, query, sort_field, sort_order, limit)
