import numpy as np

filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(
    filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df), ' of size: ', bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',
      bef_stats_df[0], '\nlast line\n', bef_stats_df[len(bef_stats_df)-1])
