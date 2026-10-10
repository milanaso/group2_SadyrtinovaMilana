from pathlib import Path

file_path = Path("sample.txt")

with open(file_path, "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is Practice 6.\n")

with open(file_path, "a") as file:
    file.write("This line was appended.\n")

print("File created and updated.")
