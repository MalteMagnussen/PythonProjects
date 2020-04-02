# Exercise 2 use meanshift on the iris dataset
from itertools import cycle
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
import pandas as pd
# PANDA SETTINGS FOR PRETTIER TERMINAL
pd.options.display.max_columns = None
pd.options.display.max_rows = None
#   1. load 'iris_data.csv' into a dataframe
iris_data = pd.read_csv("iris_csv.csv")
print("#1 read_csv")
print(iris_data.head())
#   2. get unique labels (Species column)
unique_labels = iris_data['Species'].unique()
print()
print("#2 get unique labels")
print(unique_labels)
#   3. plot with a scatter plot each iris flower sample colored by label (3 different colors)
setosa = iris_data.loc[iris_data['Species'] == unique_labels[0]]
versicolor = iris_data.loc[iris_data['Species'] == unique_labels[1]]
virginica = iris_data.loc[iris_data['Species'] == unique_labels[2]]
flowers = [setosa, versicolor, virginica]
# plt.scatter(setosa['Sepal length'],
#             setosa['Sepal width'], c='b', label='Setosa')
# plt.scatter(versicolor['Sepal length'],
#             versicolor['Sepal width'], c='r', label='versicolor')
# plt.scatter(virginica['Sepal length'],
#             virginica['Sepal width'], c='g', label='virginica')
# # plt.gray() # To add greyscale.
# plt.legend(loc='upper left')
# plt.show()
#   4. use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth
#           and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
# Så "meanshift" er centrum af den cirkel med radius "bandwidth" der i et plot dækker over flest punkter


plt.figure(1)
plt.clf()

colors = cycle('brg')
for flower, col in zip(flowers, colors):
    print("\n\n NEW FLOWER:")
    df = flower.drop(['Species'], axis=1)
    df = df.drop(['Petal length'], axis=1)
    df = df.drop(['Petal width'], axis=1)
    # setosa_shift = setosa.drop(['Species'], axis=1)
    # versicolor_shift = versicolor.drop(['Species'], axis=1)
    # virginica_shift = virginica.drop(['Species'], axis=1)
    # df = np.array([setosa_shift['Sepal length'].tolist(), setosa_shift['Sepal width'].tolist(),
    #                versicolor_shift['Sepal length'].tolist(
    # ), versicolor_shift['Sepal width'].tolist(),
    #     virginica_shift['Sepal length'].tolist(), virginica_shift['Sepal width'].tolist()])
    print("\n\n", df, "\n\n")
    bandwidth = estimate_bandwidth(df, quantile=0.5)
    print("\nBandwidth", bandwidth)
    ms = MeanShift(bandwidth=bandwidth)
    clustering = ms.fit(df)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)
    #   5. print out labels, cluster centers and number of clusters (as returned from the MeanShift function
    print()
    print("labels\n", labels)
    print("number of estimated clusters : %d" % n_clusters_)
    print("cluster centers:", cluster_centers)
    #   6. create a new scatter plot where each flower is colored according to cluster label
    #   7. add a dot for the cluster centers
    #   8. Compare the 2 plots (colored by actual labels vs. colored by cluster label)
    print("labels_unique:", labels_unique)
    print("MS:", ms)

    my_members = labels == 0
    cluster_center = cluster_centers[0]
    plt.plot(df.iloc[my_members, 0], df.iloc[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

plt.title('Estimated number of clusters: 3')
plt.show()
