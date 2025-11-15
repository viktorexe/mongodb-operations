import os
from pathlib import Path

def get_folder_size_mb(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size / (1024 * 1024)

if __name__ == "__main__":
    folder_name = input("Enter folder/database name: ").strip()
    folder_path = Path(folder_name)
    
    if not folder_path.exists():
        print(f"Folder '{folder_name}' not found")
        exit(1)
    
    size_mb = get_folder_size_mb(folder_path)
    print(f"\n✓ Total size: {size_mb:.2f} MB")
