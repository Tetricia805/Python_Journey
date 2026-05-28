
from pathlib import Path

path = Path("emails")

print(path.rmdir())

# rmdir-- remove directory, mkdir = make directory

# to search for any file in the path , use the following


path = Path()

for file in path.glob("*.*"):
    print(file)  # *.* is for everything, then to find any other file u can use *.py, *.xsl, * for both files and directories
