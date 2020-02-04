import csv

filename = './befkbhalderstatkode.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        print('Row #' + str(reader.line_num) + ' ' + str(row))

        # The following line is only for the example in class
        # as the file is quite big...
        if reader.line_num > 5:  # 000:
            break

# READING CSV

ages = set([])

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        # OBS: cast to int otherwise we would read strings!
        ages.add(int(row[2]))

print(sorted(ages))
print(max(ages))
