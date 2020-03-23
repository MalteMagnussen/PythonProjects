import wget

!wget https://snap.stanford.edu/data/twitter_combined.txt.gz

!gunzip twitter_combined.txt.gz

import networkx as nx

g = nx.read_edgelist('twitter_combined.txt')

print(nx.info(g))

print('214328887' in g)

