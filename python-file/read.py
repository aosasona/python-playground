# Read a file in python
from os.path import exists as file_exists


def read_file():
    filename = input(
        "Enter the name of file you want to open and the extension... \n")

    file_exists(filename)

    if file_exists(filename):
        with open(filename, "r") as file:
            print(file.read())
    else:
        print("File does not exist")
