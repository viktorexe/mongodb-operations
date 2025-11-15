import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client

def list_databases():
    client = get_mongo_client()
    databases = client.list_database_names()
    print("\nDatabases:")
    for db in databases:
        print(f"  - {db}")
    client.close()

if __name__ == "__main__":
    list_databases()
