import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.config import get_mongo_client

def get_server_status():
    client = get_mongo_client()
    status = client.admin.command("serverStatus")
    
    print("\nServer Status:")
    print(f"Host: {status['host']}")
    print(f"Version: {status['version']}")
    print(f"Uptime: {status['uptime']} seconds")
    print(f"Connections: {status['connections']['current']}")
    
    client.close()

if __name__ == "__main__":
    get_server_status()
