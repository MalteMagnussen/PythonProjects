import os


def checkFile(fileName):
    """ Check whether or not a file exists in current repo """
    arr = os.listdir()
    for x in arr:
        if x == fileName:
            print("File already exists.")
            return True
    print("File doesn't yet exist. Creating file.")
    return False
