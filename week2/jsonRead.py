import json
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'tmp/numbers.json')

# open the file in read mode
with open(filename) as f_obj:
    de_numbers = json.load(f_obj)

print(de_numbers)
