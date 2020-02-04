# Write a program that converts the Excel spreadsheet ./iris_data.xlsx into a CSV file with the same data.
# Start with writing a unit test against which you implement your solution (see below).

# Lets begin then

# Importing and fetching the sheets

import openpyxl
import csv
import platform


if platform.system() == 'Windows':
    newline = ''
else:
    newline = None

with open('iris_csv.csv', 'w', newline=newline) as output_file:

    filename = './iris_data.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb["Fisher's Iris Data"]

    output_writer = csv.writer(output_file)

    for row in sheet:
        rowCells = []
        for cell in row:
            rowCells.append(cell.value)
        output_writer.writerow(rowCells)
