import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

names = ["Target", "Balance", "Scale", "Weight", "Distance"]

with open("balance-scale.data", "r") as f:

    df = pd.read_csv(f, header=None, names=names)
    print(df.head())
    # Splitting the data
    X = df.values[:, 1:5]
    Y = df.values[:, 0]
    # Why? What are we doing here?
    print("\nX\n", X)
    print("\nY\n", Y)
