import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

myData = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])

df = pd.DataFrame(data=myData,
                  columns=['Col1', 'Col2', 'Col3'],
                  index=["Row1", "Row2", "Row3"])

print("\n", df)
print()
# print("\n", df.index)

# print("\n", df.columns)

# Make slices of data:
# 1. second column using column name
print(df[['Col2']])
print()
# third column using column index (.iloc[])
print(df.iloc[:, 2])
print()
# slice element at third row of second column (use .iloc())
print(df.iloc[2, 1])
