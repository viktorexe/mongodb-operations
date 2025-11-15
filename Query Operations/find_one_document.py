import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def find_one_document(db_name, collection_name, query):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    document = collection.find_one(query)
    
    if document:
        document['_id'] = str(document['_id'])
        print(json.dumps(document, indent=2))
    else:
        print("No document found")
    
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    query_json = input("Query (JSON): ").strip()
    query = json.loads(query_json)
    find_one_document(db_name, collection_name, query)
