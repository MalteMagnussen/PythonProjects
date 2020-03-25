from concurrent.futures import ProcessPoolExecutor
from webget import download
import networkx as nx
import gzip
import numpy as np
import os

filename = "facebook_combined.txt.gz"


def download_facebook_file():
    download_link = "https://snap.stanford.edu/data/facebook_combined.txt.gz"

    shouldDownload = True

    for index, entry in enumerate(os.scandir(".")):
        print(f"Filename of {index}:", entry.name)
        if entry.name == download_link:
            shouldDownload = False
            print(f"File already exists: {entry.name}")

    if shouldDownload == True:
        download(download_link, filename)
    else:
        print("Didn't download file, since it already exists locally.")


download_facebook_file()


# def multiprocessing(func, args, workers):
#     with ProcessPoolExecutor(workers) as ex:
#         res = ex.map(func, args)
#     return list(res)


with gzip.open(filename, "r") as f:
    print(f"Reading file")
    graph = nx.read_edgelist(f)

print(nx.info(graph))

# bash
# conda install -y networkx
# conda install -c anaconda pygraphviz

import warnings
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, write_dot


def create_graph():
    graph = nx.DiGraph()
    graph.clear()

    # add node by node, needed to add attributes...
    print(len(all_names_list))

    for idx, name_pair in enumerate(all_names_list):
        graph.add_node(idx, name=" ".join(name_pair))

    # graph.add_nodes_from(all_names_list)
    graph.add_edges_from(endorsements)

    return graph


import pygraphviz


def draw_graph(graph):
    nx.draw(
        graph,
        pos=graphviz_layout(graph),
        node_size=30,
        width=0.05,
        cmap=plt.cm.Blues,
        with_labels=True,
        node_color=range(len(graph)),
    )


# graph = create_graph()
draw_graph(graph)

# nx.write_gml(graph, './social_network.gml')


# Who is the most interesting person in our network?¶
# Likely, you are tempted to find the person in the graph, which has the highest in-degree. For example with code similar to the following.

import numpy as np

in_deg_vec = np.array([graph.in_degree(n) for n in graph.nodes()])
print(in_deg_vec)
in_deg_vec.max()  # return largest value
print(np.argmax(in_deg_vec))
idx = np.argmax(in_deg_vec)  # returns the index of the largest value
print(graph.nodes[idx]["name"])
