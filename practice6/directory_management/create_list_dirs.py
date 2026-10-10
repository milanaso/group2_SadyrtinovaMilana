from pathlib import Path
import os
import shutil

base = Path("practice6_test")
nested = base / "folder1" / "folder2"

nested.mkdir(parents=True, exist_ok=True)

(nested / "example.txt").write_text("Hello!")
(nested / "data.py").write_text("print('Hello')")

print("Current directory:", os.getcwd())

print("All items:")
for item in base.rglob("*"):
    print(item)

print("Directories:")
for item in base.rglob("*"):
    if item.is_dir():
        print(item)

print("Files:")
for item in base.rglob("*"):
    if item.is_file():
        print(item)

print("Python files:")
for item in base.rglob("*.py"):
    print(item)

print("Text files:")
for item in base.rglob("*.txt"):
    print(item)
print("Copy and move files:")

source_dir = base / "source"
destination_dir = base / "destination"

source_dir.mkdir(parents=True, exist_ok=True)
destination_dir.mkdir(parents=True, exist_ok=True)

source_file = source_dir / "example.txt"
source_file.write_text("Hello, Python!")

shutil.copy2(source_file, destination_dir / "example_copy.txt")
print("File copied.")

shutil.move(str(source_file), str(destination_dir / "example_moved.txt"))
print("File moved.")