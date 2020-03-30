import pandas as pd

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
# Task: Drop rows with missing values
# Task: what is the best bandwidth to use for our dataset? Use sklearn
# Task: Fit data to a meanshift model
# Task: How many clusters do we get
# Task: Add a column to the titanic dataframe with the cluster label for each person
# Task: Get mean values of each cluster group
# Task: Add a column with the size of each cluster group.
# Task: Write out conclusion from the aggregated data.
