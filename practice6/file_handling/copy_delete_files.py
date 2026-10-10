import shutil
from pathlib import Path

source = Path("sample.txt")
copy = Path("sample_copy.txt")
backup = Path("sample_backup.txt")

if source.is_file():
    shutil.copy2(source, copy)
    shutil.copy2(source, backup)
    print("File copied and backed up.")

    if copy.exists() and copy.is_file():
        copy.unlink()
        print("Copy deleted.")
else:
    print("Source file does not exist.")
