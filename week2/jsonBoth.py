import json

import os


def makeFilepath(thispath=""):
    filepath = thispath
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    return os.path.join(fileDir, filepath)


def dump(path, data):
    with open(path, 'w') as f_obj:
        json.dump(data, f_obj)


def load(path):
    with open(path) as f_obj:
        content = json.load(f_obj)
    return content


# Some example data taken from:
# https://adobe.github.io/Spry/samples/data_region/JSONDataSetSample.html#Example6
# example_data = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "image": {
#         "url": "images/0001.jpg",
#         "width": 200,
#         "height": 200
#     },
#     "thumbnail": {
#         "url": "images/thumbnails/0001.jpg",
#         "width": 32,
#         "height": 32
#     }
# }

# dump(path, example_data)
