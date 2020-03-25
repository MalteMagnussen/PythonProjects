from concurrent.futures import ProcessPoolExecutor
from webget import download
import networkx as nx
import gzip
import numpy as np
import os

filename = "facebook_combined.txt.gz"


def download_facebook_file():
    download_link = "https://snap.stanford.edu/data/facebook_combined.txt.gz"

    shouldDownload = False

    for entry in os.scandir("."):
        if entry.name is download_link:
            shouldDownload = True

    if shouldDownload:
        download(download_link, filename)


download_facebook_file()


# def multiprocessing(func, args, workers):
#     with ProcessPoolExecutor(workers) as ex:
#         res = ex.map(func, args)
#     return list(res)


with gzip.open(filename, "r") as f:
    graph = nx.read_edgelist(f)

print(nx.info(graph))
