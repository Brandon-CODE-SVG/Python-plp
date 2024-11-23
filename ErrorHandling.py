# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_and_write_file():
    filename = input("Enter the file name to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()

        print("File content read successfully.")

        modified_content = content.upper()

        new_filename = input("Enter the new filename to write the modified content: ")

        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        print(f"Modified content written to {new_filename} successfully.")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except IOError:
        print(f"Error: Unable to read or write the file.")
