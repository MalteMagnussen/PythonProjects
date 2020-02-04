# create a function, that can read all lines from a file and copy to another file only the lines, that starts with a number

filename = 'numberTest.txt'

numberLines = ""

with open(filename) as file_object:
    fileContent = file_object.readlines()

for x in fileContent:
    if (x[0].isdigit() and isinstance(int(x[0]), int)):
        numberLines += x

with open("numberReceiver.txt", 'w') as file_two:
    file_two.write(numberLines)
