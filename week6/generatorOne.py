# Create a generator function that can take a list of names
# as parameter and return each name.
# Get approved unisex names here:

import pandas as pd

df = pd.read_excel(
    r'Alle navne, der er godkendt som både drenge- og pigenavn per 2020-03-02.xls')
print(df)


def firstn(n):
    """Our first generator that lazy loads each requested element (as opposed to iterator, that builds the whole list in memory)"""
    num = 0
    while num < n:
        yield num
        num += 1


[x for x in firstn(10)]
