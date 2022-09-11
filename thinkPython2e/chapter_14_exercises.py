import os

# SECTION 14.4 EXERCISE:

def walk(dirname):
    """Takes a directory and prints, for said directory and any subdirectories, its
    name and its files.

    dirname: string
    """

    for (root, dirs, files) in os.walk(dirname):
        print(root)
        print(files)
        print("-----")

walk("14.4_exercise")