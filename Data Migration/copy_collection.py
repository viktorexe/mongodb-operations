import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client, get_collection

def copy_collection(source_db, source_coll, target_db, target_coll):
    client = get_mongo_client()
    source = get_collection(client, source_db, source_coll)
    target = get_collection(client, target_db, target_coll)
    
    documents = list(source.find())
    if documents:
        target.insert_many(documents)
        print(f"✓ Copied {len(documents)} documents")
    else:
        print("No documents to copy")
    
    client.close()

if __name__ == "__main__":
    source_db = input("Source database: ").strip()
    source_coll = input("Source collection: ").strip()
    target_db = input("Target database: ").strip()
    target_coll = input("Target collection: ").strip()
    copy_collection(source_db, source_coll, target_db, target_coll)
