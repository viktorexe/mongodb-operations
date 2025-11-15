import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client

def list_users(db_name):
    client = get_mongo_client()
    db = client[db_name]
    users = db.command("usersInfo")
    
    print(f"\nUsers in '{db_name}':")
    for user in users['users']:
        print(f"  - {user['user']}")
        print(f"    Roles: {user['roles']}")
    
    client.close()

if __name__ == "__main__":
    db_name = input("Database name: ").strip()
    list_users(db_name)
