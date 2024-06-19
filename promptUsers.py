# import createUsers
from createDirectories import *

def create_file_in_directory(file_name, directory):
    if directory not in directories:
        print(f"Error: '{directory}' is not a valid directory.")
        return
    
    file_path = os.path.join(directory, file_name)
    
    with open(file_path, 'w') as file:
        file.write("")  # Create an empty file
        print(f"File '{file_name}' created in directory '{directory}'.")

def prompt_user_for_file_creation():
    file_name = input("Enter the name of the file: ")
    directory = input("Enter the directory to create the file in: ")
    create_file_in_directory(file_name, directory)

# Run the user prompt function
prompt_user_for_file_creation()

