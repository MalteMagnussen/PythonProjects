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
    # Make a new scatter plot with datapoints of weights vs heights. Choose different colors for rats and mice
    def scatterplotRodents():
        # Mice
        mice = df.loc[df["type"] == "mouse"]
        plt.scatter(mice["weight"], mice["height"], c="red")
        # Rats
        rats = df.loc[df["type"] == "rat"]
        plt.scatter(rats["weight"], rats["height"], c="blue")
        plt.xlabel("weight")
        plt.ylabel("height")
        plt.title("red is mice, blue is rats")
        plt.show()

    scatterplotRodents()


def activation_function(x):
    """
    Step function to respond with y = 1 or -1
    Parameter:
    x: An x (numeric) value that will have a corresponding y value of 1 or -1
    """
    # Look at the activation_function and plot the y-values for each x from -5,5 spaced with 0.5
    if x < 0:
        return -1
    else:
        return 1


rnge = np.linspace(-5.5, 5.5, num=23)
print("rnge:", rnge)
values = [activation_function(i) for i in rnge]
print("values: ", values)
# plt.plot(values)
# plt.axis([-10, 9, -2, 2])
# plt.show()


def perceptron(inp, weights):
    """
    Given a list of input (x) values and a list of weights, 
    calculates the dot product of the 2 lists and returns 1 or -1 (fire or don't)
    Parameters:
    inp: vector of input predictors
    weights: vector of weights to be ajusted for precise prediction of output.
    """
    # Change the perceptron method from the notebook to use the numpy.dot() method in line 12 instead of the lengthy sum() function
    dot_product = np.dot(inp, weights)
    output = activation_function(dot_product)
    return output
