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
