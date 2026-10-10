
from pathlib import Path
import shutil
import string
import os

base = Path("practice6_test")
base.mkdir(exist_ok=True)

#1
nested = base / "folder1" / "folder2"
nested.mkdir(parents=True, exist_ok=True)

(nested / "example.txt").write_text("Hello!\nPython Practice\n")
(nested / "data.py").write_text("print('Hello')")

print("All files and directories:")
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


#2
path = nested / "example.txt"

print("Exists:", os.path.exists(path))
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))


#3
if path.exists():
    print("Filename:", path.name)
    print("Directory:", path.parent)
else:
    print("File does not exist.")


#4
with open(path, "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))


#5
items = ["Apple", "Banana", "Orange"]

list_file = base / "list.txt"

with open(list_file, "w") as file:
    for item in items:
        file.write(item + "\n")


#6
letters_dir = base / "letters"
letters_dir.mkdir(exist_ok=True)

for letter in string.ascii_uppercase:
    (letters_dir / f"{letter}.txt").touch()


#7
source = list_file
destination = base / "list_copy.txt"

if source.is_file():
    shutil.copyfile(source, destination)
    print("File copied.")


#8
target = base / "list_copy.txt"

if target.exists() and target.is_file():
    if os.access(target, os.W_OK):
        target.unlink()
        print("File deleted.")
    else:
        print("No permission to delete the file.")
else:
    print("File does not exist.")
