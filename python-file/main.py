#Main python file fro this project

from write import write_file
from read import read_file

action: int = input('What do you want to do today? (Enter a corresponding answer) \n \t 1. Create a new file \n\t 2. Read a file \n')

if action == "1":
    write_file()
elif action == "2":
    read_file()
else:
    print("Chief, that was not in the options!")