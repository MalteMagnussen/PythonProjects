# Create a generator function that can take a list of names
# as parameter and return each name.
# Get approved unisex names here:

import pandas as pd

df = pd.read_excel(
    'Alle navne, der er godkendt som både drenge- og pigenavn per 2020-03-02.xls')
# df = pd.read_excel(
#     "https://ast.dk/_namesdb/export/names?format=xls&gendermask=4")
# print(df)


def firstn(n):
    num = 0
    while num < len(n):
        yield n[num]
        num += 1


#Generator = g
g = firstn(df["Names"].values.tolist())
print(next(g))


print("\n_____DF GENERATOR_____\n")

generator = df.iterrows()
for idx, row in generator:
    if idx < 4:
        print(row["Names"])

# for x in range(0, 4):
#     print(next(generator))
