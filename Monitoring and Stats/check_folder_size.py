import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from Utilities.helpers import get_folder_size_mb

def check_folder_size(folder_path):
    if not Path(folder_path).exists():
        print(f"Folder '{folder_path}' not found")
        return
    
    size_mb = get_folder_size_mb(folder_path)
    print(f"\n✓ Total size: {size_mb:.2f} MB")

if __name__ == "__main__":
    folder_path = input("Enter folder path: ").strip()
    check_folder_size(folder_path)
