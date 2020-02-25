import numpy as np
import pandas as pd

# Pandas Series with multiple data types
s = pd.Series([1, 3, 5, np.nan, 'seks', 8])
print(s, '\n---------------------')
# in pd.Series we can provide any keys we like to the data
s = pd.Series(['seks', 'fem', 'fire'], [6, 5, 4])
print(s)
