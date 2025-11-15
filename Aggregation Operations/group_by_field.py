import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def group_by_field(db_name, collection_name, field):
    client = get_mongo_client()
    collection = get_collection(client, db_name, collection_name)
    
    pipeline = [
        {"$group": {"_id": f"${field}", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    
    results = list(collection.aggregate(pipeline))
    print(json.dumps(results, indent=2))
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    collection_name = input("Collection name: ").strip()
    field = input("Field to group by: ").strip()
    group_by_field(db_name, collection_name, field)
