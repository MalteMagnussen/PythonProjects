# ## Exercise 2
# Create a module called utils.py and put the following functions inside:
# 1. first function takes a path to a folder and writes all filenames in the folder to a specified output file
# 2. second takes a path to a folder and write all filenames recursively (files of all sub folders to)
# 3. third takes a list of filenames and print the first line of each
# 4. fourth takes a list of filenames and print each line that contains an email (just look for @)
# 5. fifth takes a list of md files and writes all headlines (lines starting with #) to a file
# Make sure your module can be called both from cli and imported to another module
# Create a new module that imports utils.py and test each function.
import os
from utils import filenamesToFolder, allFileNames, printFirstLine, findEmails, getHeadlines

# Test of number 1
# filenamesToFolder("PythonProjects/week2/Exercises", "PythonProjects/week2/Exercises/testFilenamesToFolder.txt")

# Test of number 2
# allFileNames(os.getcwd)

# Test of number 3
# printFirstLine(["PythonProjects/week2/Exercises/testFilenamesToFolder.txt",
#                "PythonProjects/week2/Exercises/testFile.txt"])

# Test of number 4
# findEmails(["PythonProjects/week2/Exercises/moreEmails.txt",
#             "PythonProjects/week2/Exercises/emails.txt"])

# Test of number 5
# getHeadlines(["PythonProjects/week2/Exercises/one.md",
#               "PythonProjects/week2/Exercises/two.md"])
