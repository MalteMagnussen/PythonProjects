# How to import this module: from .. import checkFile

import os


def checkFile(fileName):
    """ Check whether or not a file exists in current repo """
    arr = os.listdir()
    for x in arr:
        if x == fileName:
            return true:
    return false
