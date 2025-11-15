import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def find_documents(db_name, collection_name, query, limit=10):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    documents = list(collection.find(query).limit(limit))
    
    for doc in documents:
        doc['_id'] = str(doc['_id'])
    
    print(json.dumps(documents, indent=2))
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    query_json = input("Query (JSON, empty for all): ").strip()
    query = json.loads(query_json) if query_json else {}
    limit = int(input("Limit (default 10): ").strip() or 10)
    find_documents(db_name, collection_name, query, limit)
