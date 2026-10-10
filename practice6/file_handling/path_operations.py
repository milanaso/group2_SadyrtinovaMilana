import os
from pathlib import Path

path = Path("sample.txt")

print("Exists:", path.exists())

if path.exists():
    print("Filename:", path.name)
    print("Directory:", path.parent)

print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
print("Executable:", os.access(path, os.X_OK))
