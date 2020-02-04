# You can open a file in read mode ('r'), write mode ('w'), append mode ('a'),
# or a mode that allows you to read and write to the file ('r+').
# If you omit the mode argument, Python opens the file in read-only mode by default.

import checkFile

filename = 'msg.txt'
testText = "TEST WRITING"

if not (checkFile.checkFile(filename)):
    with open(filename, 'w') as file_object:
        print("Writing {} to {}".format(testText, filename))
        file_object.write(testText)
else:
    print("Didn't write")
