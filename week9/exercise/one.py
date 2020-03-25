from concurrent.futures import ProcessPoolExecutor
from webget import download
import networkx as nx
import gzip
import numpy as np
import os
import warnings
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import pygraphviz

# Thomas Hartmann exercise

# Exercise 1
print("Exercise 1")
filename = "facebook_combined.txt.gz"


def download_facebook_file():
    download_link = "https://snap.stanford.edu/data/facebook_combined.txt.gz"

    shouldDownload = True

    if os.path.isfile(filename):
        print("File exists")
    else:
        download(download_link, filename)


download_facebook_file()

print()
print()
# def multiprocessing(func, args, workers):
#     with ProcessPoolExecutor(workers) as ex:
#         res = ex.map(func, args)
#     return list(res)


# Exercise 2
print("Exercise 2")
with gzip.open(filename, "r") as f:
    print(f"Reading file")
    graph = nx.read_edgelist(f)

print(nx.info(graph))
# g.degree giver antallet af edges som støder op mod noden.
deg_vec = np.array([graph.degree(n) for n in graph.nodes()])
# deg_vac.max() giver mig bare det højeste tal af numpy arrayet
max_ind_deg = deg_vec.max()
# np.argmax() giver indexet af det højeste tal af numpy arrayet
index_name = list(graph.nodes())[np.argmax(deg_vec)]
print(
    "The node {} has the most connections with {} connections".format(
        index_name, len(list(graph.neighbors(index_name)))
    )
)

print()
print()
print("Exercise 3")
# Exercise 3
nx.draw_shell(graph)

# bash
# conda install -y networkx
# conda install -c anaconda pygraphviz


# def draw_graph(graph):
#     nx.draw(
#         graph,
#         pos=graphviz_layout(graph),
#         node_size=30,
#         width=0.05,
#         cmap=plt.cm.Blues,
#         with_labels=True,
#         node_color=range(len(graph)),
#     )


# graph = create_graph()
# draw_graph(graph)
# nx.draw(graph)

# nx.write_gml(graph, './social_network.gml')


# Who is the most interesting person in our network?¶
# Likely, you are tempted to find the person in the graph, which has the highest in-degree. For example with code similar to the following.


# in_deg_vec = np.array([graph.in_degree(n) for n in graph.nodes()])
# print(in_deg_vec)
# in_deg_vec.max()  # return largest value
# print(np.argmax(in_deg_vec))
# idx = np.argmax(in_deg_vec)  # returns the index of the largest value
# print(graph.nodes[idx]["name"])
