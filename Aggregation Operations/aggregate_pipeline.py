import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def aggregate_pipeline(db_name, collection_name, pipeline):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    results = list(collection.aggregate(pipeline))
    
    for doc in results:
        if '_id' in doc:
            doc['_id'] = str(doc['_id'])
    
    print(json.dumps(results, indent=2))
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    pipeline_json = input("Pipeline (JSON array): ").strip()
    pipeline = json.loads(pipeline_json)
    aggregate_pipeline(db_name, collection_name, pipeline)
