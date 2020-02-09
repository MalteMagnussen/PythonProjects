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
import argparse
import sys
from pathlib import Path


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

    return os.listdir(pathToFolder)


def allFileNames(path):
    '''
    2. second takes a path to a folder and write all filenames recursively (files of all sub folders to)

    Parameters: 

        path (str): The path to the root folder you want to get all filenames from.

    '''

    # Getting the current work directory (cwd)
    thisdir = os.getcwd()

    # r=root, d=directories, f = files
    for r, d, f in os.walk(thisdir):
        for file in f:
            print(os.path.join(r, file))
        for direct in d:
            print(os.path.join(r, direct))


# allFileNames(os.getcwd())

def printFirstLine(listOfFiles):
    """
    third takes a list of filenames and print the first line of each

    Parameters:

        listOfFiles (list): List of Filenames
    """

    for fileName in listOfFiles:
        with open(fileName) as file_object:
            print(file_object.readlines().pop(0).rstrip())


def findEmails(listOfFiles):
    '''
    fourth takes a list of filenames and print each line that contains an email (just look for @)

    Parameters:

        listOfFiles (list): List of Filenames
    '''

    for fileName in listOfFiles:
        with open(fileName) as file_object:
            for line in file_object.readlines():
                if ("@" in line):
                    print(line.rstrip())


def getHeadlines(listOfMdFiles):
    '''
    fifth takes a list of md files and writes all headlines (lines starting with #) to a file

    Parameters:

        listOfMdFiles (list): List of Filenames
    '''

    for fileName in listOfMdFiles:
        with open(fileName) as file_object:
            for line in file_object.readlines():
                if (line[0] == "#"):
                    print(line.rstrip())


parser = argparse.ArgumentParser(
    description='A program that downloads a URL and stores it locally')

# Positional arg
parser.add_argument('func', help='name of the def you wanna run')

if __name__ == '__main__':
    args, restArgs = parser.parse_known_args()

    nameOfDef = args.func

    if (nameOfDef == "filenamesToFolder"):
        filenamesToFolder(restArgs[0], restArgs[1])

    if (nameOfDef == "allFileNames"):
        allFileNames(restArgs[0])
