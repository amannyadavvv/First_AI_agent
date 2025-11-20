import os

filename = "file.txt"

if os.path.exists(filename):
    print("Yes, file exists")
else:
    with open(filename, "w") as f:
        f.write("This file was created because it didn't exist.")
    print("File created!")
