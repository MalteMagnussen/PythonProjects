# ## Exercise 1
# 1. Create a python file with 3 functions:
#   1. `def print_file_content(file)` that can print content of a csv file to the console
#   2. `def write_list_to_file(output_file, lst)` that can take a list of tuple and write each element to a new line in file
#     1. rewrite the function so that it gets an arbitrary number of strings instead of a list
#   3. `def read_csv(input_file)` that take a csv file and read each row into a list
# 2. Add a functionality so that the file can be called from cli with 2 arguments
#   1. path to csv file
#   2. an argument `--file file_name` that if given will write the content to file_name or otherwise will print it to the console.
# 3. Add a --help cli argument to describe how the module is used
from PythonProjects.utils import webget
import argparse
import csv


def print_file_content(file):
    """1. `def print_file_content(file)` that can print content of a csv file to the console"""
    # It should be able to print content of a csv file to console.

    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:
            print(str(row))

# testing 1.
# filename = './iris_csv.csv'
# print_file_content(filename)
# ^Works


def write_list_to_file(output_file, *args):
    """`def write_list_to_file(output_file, lst)` 
    that can take a list of tuple 
    and write each element to a new line in file"""
    # rewrite the function so that it gets an arbitrary number of strings instead of a list

    toFile = ""
    for x in args:
        toFile += x + "\n"

    with open(output_file, 'w') as file_object:
        print("Writing {} to {}".format(toFile, output_file))
        file_object.write(toFile)


# Testing write_list_to_file
# testStringOne = "First Line"
# testStringTwo = "Second Line"
# testStringThree = "Third Line"

# filename = "testFile.txt"

# print("\n___________________________________________\nSecond Test::\n")
# write_list_to_file(filename, testStringOne, testStringTwo, testStringThree)
# ^Works

# `def read_csv(input_file)` that take a csv file and read each row into a list


def read_csv(input_file):
    list = []
    with open(input_file) as f:
        reader = csv.reader(f)

        for row in reader:
            list.append(row)

    return list


# print("\n___________________________________________\nThird Test::\n")
# filename = "iris_csv.csv"
# print(read_csv(filename))

# 2. Add a functionality so that the file can be called from cli with 2 arguments
#   1. path to csv file
#   2. an argument `--file file_name` that if given will write the content to file_name or otherwise will print it to the console.
# Add a --help cli argument to describe how the module is used
parser = argparse.ArgumentParser(
    description='A program that can handle CSV')

# Positional arg
parser.add_argument('path', help='path to csv file')

# Optional Arg [- , --]
parser.add_argument('-f', '--file_name',
                    help='if given will write the content to file_name or otherwise will print it to the console.')


args = parser.parse_args()


def listToString(s):
    str1 = ","
    return (str1.join(s))


if __name__ == '__main__':
    args = parser.parse_args()

    path = args.path

    myContent = read_csv(path)

    content = ""

    for x in myContent:
        content += listToString(x) + "\n"

    if (args.file_name != None):
        file_name = args.file_name
        # write the content to file_name
        with open(file_name, 'w') as file_object:

            print("Writing {} to {}".format(content, file_name))
            file_object.write(content)
    else:
        # Print it to console
        print_file_content(path)
