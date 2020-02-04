import json
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
filename = os.path.join(fileDir, 'tmp/numbers.json')

numbers = {1: 'a', 2: [1, 2, 3]}

with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
