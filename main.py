import os
from pathlib import Path

def create_numbered_folders():
    print("=== Folder Creator ===")
    
    # Get user input
    base_name = input("Enter the base folder name: ").strip()
    while True:
        try:
            num_folders = int(input("Enter the number of folders to create: "))
            if num_folders < 1:
                print("Please enter a number greater than 0")
                continue
            break
        except ValueError:
            print("Please enter a valid number")
    
    # Create folders
    created_count = 0
    for i in range(1, num_folders + 1):
        folder_name = f"{base_name}_{i}"
        try:
            Path(folder_name).mkdir(exist_ok=False)
            print(f"Created folder: {folder_name}")
            created_count += 1
        except FileExistsError:
            print(f"Folder already exists: {folder_name} (skipped)")
    
    print(f"\nSuccessfully created {created_count} of {num_folders} requested folders")

if __name__ == "__main__":
    create_numbered_folders()