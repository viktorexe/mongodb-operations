import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def find_with_projection(db_name, collection_name, query, projection, limit=10):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    documents = list(collection.find(query, projection).limit(limit))
    
    for doc in documents:
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])
    
    print(json.dumps(documents, indent=2))
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    query_json = input("Query (JSON): ").strip()
    projection_json = input("Projection (JSON, e.g. {'field': 1}): ").strip()
    query = json.loads(query_json)
    projection = json.loads(projection_json)
    limit = int(input("Limit (default 10): ").strip() or 10)
    find_with_projection(db_name, collection_name, query, projection, limit)
