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
# Task: Get mean values of each cluster group
# Task: Add a column with the size of each cluster group.
# Task: Write out conclusion from the aggregated data.
