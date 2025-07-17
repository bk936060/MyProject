import os

# Specify the directory path
directory_path = input("Enter the directory path: ")

# Check if the path exists
if os.path.exists(directory_path):
    # Get the list of files and directories
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
else:
    print("The specified path does not exist.")
