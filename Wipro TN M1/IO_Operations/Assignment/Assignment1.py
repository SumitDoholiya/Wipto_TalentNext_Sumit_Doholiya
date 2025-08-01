"""Write a program to read the entire content from a txt file and display it to the user."""

# Program to read and display content of a text file

# Replace 'example.txt' with your file name
file_path = 'example.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:\n")
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
