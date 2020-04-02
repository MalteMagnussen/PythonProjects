# Exercise 2 use meanshift on the iris dataset

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


plt.scatter(setosa['Sepal length'],
            setosa['Sepal width'], c='b', label='Setosa')
plt.scatter(versicolor['Sepal length'],
            versicolor['Sepal width'], c='r', label='versicolor')
plt.scatter(virginica['Sepal length'],
            virginica['Sepal width'], c='g', label='virginica')
# plt.gray() # To add greyscale.
plt.legend(loc='upper left')
plt.show()


#   4. use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth
#           and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result

#   5. print out labels, cluster centers and number of clusters (as returned from the MeanShift function

#   6. create a new scatter plot where each flower is colored according to cluster label

#   7. add a dot for the cluster centers

#   8. Compare the 2 plots (colored by actual labels vs. colored by cluster label)
