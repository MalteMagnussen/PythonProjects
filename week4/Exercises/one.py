import numpy as np
import matplotlib.pyplot as plt

# Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
filename = './befkbhalderstatkode.csv'

data = np.genfromtxt(
    filename, delimiter=',', dtype=np.uint, skip_header=1)

# Using this data:
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}
# Find out how many people lived in each of the 11 areas in 2015

# AAR,BYDEL,ALDER,STATKODE,PERSONER


def opgaveEt():
    # Counts up number of people living in each area
    exercise_one = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
                    6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 99: 0}

    year = data[data[:, 0] == 2015]
    for x in neighb.keys():
        neighborhood = year[year[:, 1] == x]

        people = neighborhood[:, 4]
        number = sum(people)
        exercise_one[x] = number

    prebardata = {}

    for x in exercise_one.keys():
        print(""+str(neighb[x])+": "+str(exercise_one[x]))
        prebardata[neighb[x]] = exercise_one[x]

    # Make a bar plot to show the size of each city area from the smallest to the largest

    bardata = {k: v for k, v in sorted(
        prebardata.items(), key=lambda item: item[1])}
    plt.figure()

    # First arg is X, second is Y. Then options.
    plt.bar(list(bardata.keys()), list(bardata.values()), linewidth=5)

    # Set chart title and label axes.
    plt.title("Size of each city area.", fontsize=24)
    plt.xlabel("Area", fontsize=14)
    plt.ylabel("People", fontsize=14)
    #plt.ylim([0, 35])
    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


opgaveEt()
