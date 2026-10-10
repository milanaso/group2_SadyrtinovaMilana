from pathlib import Path

file_path = Path("sample.txt")

with open(file_path, "r") as file:
    content = file.read()
    print(content)

with open(file_path, "r") as file:
    print("First line:", file.readline().strip())

with open(file_path, "r") as file:
    lines = file.readlines()
    print("All lines:", lines)
    print("Number of lines:", len(lines))
