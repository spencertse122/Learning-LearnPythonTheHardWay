# Importing libraries
from sys import argv

# Reading in files, and parsing the filename into the script from terminal
script, filename = argv

# Opening the file
txt = open(filename)

# printing the filename with a formatter
print(f"Here's your file {filename}:")
# printing the text file
print(txt.read())

# # type the filename again
# print("Type the filename again:")
# # define file_again variable witha a prompt
# file_again = input("> ")
#
# # opening the second file (it will be the same one if you type in the same name)
# txt_again = open(file_again)
#
# # printing out the text document using .read() function
# print(txt_again.read())
