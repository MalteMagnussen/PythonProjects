# ## Exercise 2
# Create a module called utils.py and put the following functions inside:
# 1. first function takes a path to a folder and writes all filenames in the folder to a specified output file
# 2. second takes a path to a folder and write all filenames recursively (files of all sub folders to)
# 3. third takes a list of filenames and print the first line of each
# 4. fourth takes a list of filenames and print each line that contains an email (just look for @)
# 5. fifth takes a list of md files and writes all headlines (lines starting with #) to a file
# Make sure your module can be called both from cli and imported to another module
# Create a new module that imports utils.py and test each function.

# Imports
import os
import openpyxl
import csv
import platform

if platform.system() == 'Windows':
    newline = ''
else:
    newline = None


def filenamesToFolder(pathToFolder, outputFile):
    """
    1. first function takes a path to a folder and writes all filenames in the folder to a specified output file

    Parameters:

        pathToFolder (str): The Path to the Folder you want all filenames from.

        outputFile (str): The Path and filename of the file you wish to contains filenames from <pathToFolder>

    Returns:

        list:all filenames in the folder

    Test:

        # filenamesToFolder("PythonProjects/week2/Exercises",
        #                   "PythonProjects/week2/Exercises/testFilenamesToFolder.txt")

    """

    with open(outputFile, 'w', newline=newline) as file_object:
        file_object.write('\n'.join(os.listdir(pathToFolder)))

    return os.listdir(pathToFolder))
