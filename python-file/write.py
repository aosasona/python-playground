#Writing files in python

def write_file():
    filename = input("Enter a filename with extension... \n")
    textContent = input("Enter the file's content... \n")

    with open(filename, "w") as file:
        file.write(textContent)

    print(f"{filename} has been created")