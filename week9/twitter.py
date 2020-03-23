import webget
import networkx as nx
import gzip
import numpy as np

# webget.download("https://snap.stanford.edu/data/twitter_combined.txt.gz")

with gzip.open("twitter_combined.txt.gz", "r") as f:
    graph = nx.read_edgelist(f)


print(nx.info(graph))

print("214328887" in graph)

# in_deg_vec = np.array([graph.in_degree(n) for n in graph.nodes()])
# max_ind_deg = in_deg_vec.max()

# print(np.argmax(in_deg_vec))
# print(graph.node[np.argmax(in_deg_vec)]["name"])

# d = 0.85
# n = graph.number_of_nodes()
# sub_term = (1 - d) / n

# def page_rank(p):

#     page_rank = sub_term  + (d * pass)
#     return page_rank

nodes_list = np.array(__builtins__.list(graph.nodes()))
most_interesting = nodes_list[idx_most]
print(f"most interesting node: {most_interesting}")
