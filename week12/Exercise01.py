import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib
import matplotlib.pyplot as plt

# weight;height;type
# 233.4799204165095;23.514129929623852;rat
# 231.32446731816555;26.03382997978225;rat
# 17.906954059999567;6.846576762459397;mouse
# 230.276522831171;24.077799766119398;rat
# 20.36059265800554;6.6059829255227;mouse
# 21.60538751773697;6.812460032530713;mouse

# So we want to predict if its a rat or mouse, based on weight and height.
# So we have to split off the rat / mouse column

with open("rodents.csv", "r") as f:

    df = pd.read_csv(f, sep=";")
    print(df.head())
    # Splitting the data
    weightHeight = df.values[:, 0:2]
    rodentType = df.values[:, 2]
    # print("\nWeight and Height\n", weightHeight)
    # print("\ntype of rodent\n", rodentType)


def activation_function(x):
    """
    Step function to respond with y = 1 or -1
    Parameter:
    x: An x (numeric) value that will have a corresponding y value of 1 or -1
    """
    if x < 0:
        return -1
    else:
        return 1


rnge = np.linspace(-10.0, 10.0, num=1000)
print(rnge[0:5])
values = [activation_function(i) for i in rnge]
plt.plot(rnge, values)
plt.axis([-10, 9, -2, 2])
plt.show()
