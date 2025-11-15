import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client

def drop_database(db_name):
    client = get_mongo_client()
    confirm = input(f"Are you sure you want to drop '{db_name}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        client.drop_database(db_name)
        print(f"✓ Database '{db_name}' dropped")
    else:
        print("Operation cancelled")
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    drop_database(db_name)
