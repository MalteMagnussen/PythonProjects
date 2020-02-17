import numpy as np

filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(
    filename, delimiter=',', dtype=np.uint, skip_header=1)
print(type(bef_stats_df), ' of size: ', bef_stats_df.size)
print('The skip_header=1 means that we have only the data\n\nfirst line:\n',
      bef_stats_df[0], '\nlast line\n', bef_stats_df[len(bef_stats_df)-1])

dd = bef_stats_df
mask = (dd[:, 0] == 1998)  # for all rows filter column/index = 0 to be 1998
dd[mask]

mask = (dd[:, 0] == 2015) & (dd[:, 2] == 18) & (dd[:, 3] == 5100)
print(dd[mask])
# plt.axis([0,10,300,600])
#plt.bar(dd[:,1], dd[:,4])
np.sum(dd[mask][:, 4])
# plt.show()
