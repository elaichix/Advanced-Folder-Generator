import os
from pathlib import Path
from datetime import datetime

def create_numbered_folders():
    print("\n=== Advanced Folder Creator ===")
    
    # Get base configuration
    base_name = input("Enter base folder name (e.g., 'project'): ").strip()
    location = input(f"Where to create? [Press Enter for current directory or enter path]: ").strip()
    
    # Get folder count with validation
    while True:
        try:
            num_folders = int(input("Number of folders to create: "))
            if num_folders < 1:
                print("Please enter a number ≥ 1")
                continue
            break
        except ValueError:
            print("Invalid number! Please try again.")

    # Advanced options
    print("\nAdditional Options:")
    print("1. Simple numbering (project_1, project_2)")
    print("2. Zero-padded numbering (project_001, project_002)")
    print("3. Date-based folders (project_2023-12-25)")
    choice = input("Choose numbering style [1-3, default=1]: ").strip() or "1"
    
    # Create folders
    created = 0
    for i in range(1, num_folders + 1):
        if choice == "1":
            folder_name = f"{base_name}_{i}"
        elif choice == "2":
            folder_name = f"{base_name}_{i:03d}"  # 001, 002, etc.
        elif choice == "3":
            date_str = datetime.now().strftime("%Y-%m-%d")
            folder_name = f"{base_name}_{date_str}_{i}"
        
        target_path = os.path.join(location, folder_name) if location else folder_name
        
        try:
            Path(target_path).mkdir(parents=True, exist_ok=False)
            print(f"✓ Created: {target_path}")
            created += 1
        except FileExistsError:
            print(f"⚠ Already exists: {target_path}")
        except PermissionError:
            print(f"✗ Permission denied: {target_path}")
            break
    
    print(f"\nResults: Created {created}/{num_folders} folders")
    print(f"Location: {os.path.abspath(location) if location else os.getcwd()}")

if __name__ == "__main__":
    while True:
        create_numbered_folders()
        if input("\nCreate more folders? (y/n): ").lower() != 'y':
            print("Goodbye! 👋")
            break