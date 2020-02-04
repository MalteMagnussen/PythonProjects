import os
# create a function in python, that can read all names of files in a folder, when given the full path to the folder


def readNames(path):
    """ 
    :param path: str
        Absolute path to directory

    returns array of all filenames at path 
    """
    print(os.listdir(path))
    return os.listdir(path)
