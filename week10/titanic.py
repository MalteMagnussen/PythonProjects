import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None

# Task: Get the data on people on the Titanic, their class, sex age, ticket price and whether they survived.
# Answer: I manually downloaded the .zip file and extracted the files.

# Task: Load into pandas dataframe.
# Answer:
titanic_data = pd.read_csv("train.csv")
print("read_csv")
print(titanic_data.head())

# Task: Drop the PassengerId, Name, Ticket, Cabin columns from the dataframe
# Answer:
# inplace=true er at den ændrer titanic_data, i stedet for at oprette en ny og så returnere den
titanic_data.drop(["PassengerId", "Name", "Ticket", "Cabin"], "columns", inplace=True)
print()
print(".drop inplace=true")
print(titanic_data.head())


# Task: Change sex column into 0 or 1
# Answer:
from sklearn import preprocessing

# Convert gender to 0 or 1
label_enc = preprocessing.LabelEncoder()
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html
titanic_data["Sex"] = label_enc.fit_transform(titanic_data["Sex"].astype(str))
print()
print("Gender converted to 0 and 1")
print(titanic_data.head())


# Task: One-hot-encode the Embarked column (3 different ports in England)
# Answer:
# One-hot encoding of 'Embarked' with pd.get_dummies
# one-hot encoding:
# Imagine n features. One-hot encoding means setting one feature to 1 and the rest to 0.
titanic_data = pd.get_dummies(titanic_data, columns=["Embarked"])
print()
print("One hot encoding")
print(titanic_data.head())


# Task: Drop rows with missing values
# Find missing values in the data and drop those rows:
print()
print("rows before drop n/a", len(titanic_data))
# Denne linje gør egentlig ikke noget ved datasettet.
# Det er bare for at få vist alle de rækker hvor der er null værdier i.
# Prøv at printe missing så kan de se at du får alle de rækker
# hvor der er passagerer der ikke har en alder opgivet
missing = titanic_data[titanic_data.isnull().any(axis=1)]
print()
print("missing")
print(missing.head())
# Denne linje er den der dropper alle rækker med null værdier i
titanic_data = titanic_data.dropna()
print()
print("rows after", len(titanic_data))
# print(titanic_data.head())


# Task: what is the best bandwidth to use for our dataset? Use sklearn
# what is the best bandwidth to use for our dataset?
# The smaller values of bandwith result in tall skinny kernels & larger values result in short fat kernels.

# Bandwith er størrelsen på det vindue der kører ned over feature spacet
# og leder efter den højeste tæthed af nabo punkter (vektorer)
from sklearn.cluster import estimate_bandwidth

# Det kan være svært at se ud af data hvad der er den optimale vinduestørrelse,
# så derfor har vi metoden til (baseret på vores data)
# at give os den estimerede bedst egnede vinduesstørrelse
print()
print("Estimate Bandwidth")
bandwidth = estimate_bandwidth(titanic_data)
print(bandwidth)


# Task: Fit data to a meanshift model
from sklearn.cluster import MeanShift
import numpy as np

# Så "meanshift" er centrum af den cirkel med radius "bandwidth" der i et plot dækker over flest punkter
analyzer = MeanShift(bandwidth=30)
fit = analyzer.fit(titanic_data)
print()
print("fit\n", fit)
labels = analyzer.labels_
print()
print("labels\n", labels)
uniqueLabels = np.unique(labels)
print("\n\nnp.unique(labels)\n", uniqueLabels)


# Task: How many clusters do we get
print()
print("Number of clusters:")
numberOfClusters = len(uniqueLabels)
print(numberOfClusters)

# Task: Add a column to the titanic dataframe with the cluster label for each person
# We will add a new column in dataset which shows the cluster the data of a particular row belongs to.
print()
titanic_data["cluster_group"] = np.nan
data_length = len(titanic_data)
for i in range(data_length):  # loop 714 rows
    titanic_data.iloc[i, titanic_data.columns.get_loc("cluster_group")] = labels[
        i
    ]  # set the cluster label on each row
print("Data frame with cluster group")
print(titanic_data.head())


# Task: Get mean values of each cluster group
print()
print("Mean values of each cell. ")
print(titanic_data.describe())


print()
# Task: Add a column with the size of each cluster group.
# Grouping passengers by Cluster
titanic_cluster_data = titanic_data.groupby(["cluster_group"]).mean()
# Count of passengers in each cluster
titanic_cluster_data["Counts"] = pd.Series(
    titanic_data.groupby(["cluster_group"]).size()
)
print("Titanic cluster data")
print(titanic_cluster_data)



# Task: Write out conclusion from the aggregated data.

# Conclusion
# 1. Cluster 0
#   * Have 558 passengers
#   * Survival rate is 33%(very low) means most of them didn't survive
#   * They belong to the lower classes 2nd and 3rd class mostly and are mostly male .
#   * The average fare paid is $15
# 2. Cluster 1
#   * Have 108 passengers
#   * Survival rate is 61% means a little more than half of them survived
#   * They are mostly from 1st and 2nd class
#   * The average fare paid is $65
# 3. Cluster 2 i.e the 3rd Cluster
#   * Have 30 passengers
#   * Survival rate is 73% means most of them survived
#   * They are mostly from 1st class
#   * The average fare paid is $131 (high fare)
# 4. Cluster 3 i.e the 4th Cluster
#   * Have 15 passengers
#   * Survival rate is 73% means most of them survived
#   * They are mostly from 1st class and are mostly female
#   * The average fare paid is $239 (which is far higher than the 1st cluster average fare)
#   * The last cluster has just 3 datapoints so it is not that significant hence we can ignore for data analysis
