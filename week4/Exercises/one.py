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
    # plt.ylim([0, 35])
    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


# opgaveEt()

# Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
def over65():
    twentyFifteen = data[data[:, 0] == 2015]
    age = twentyFifteen[twentyFifteen[:, 2] > 65]
    copenhagen = age[age[:, 1] != 99]
    print("65 year olds in Copenhagen in 2015: "+str(sum(copenhagen[:, 4])))
    # How many of those were from the other nordic countries (not dk)
    # 5104 == Finland
    # 5110 == Norge
    # 5120 == Sverige
    finish = copenhagen[copenhagen[:, 3] == 5104]
    norway = copenhagen[copenhagen[:, 3] == 5110]
    sweden = copenhagen[copenhagen[:, 3] == 5120]
    print("of those, how many are from Nordic Countries: " +
          str(sum(finish[:, 4])+sum(norway[:, 4])+sum(sweden[:, 4])))


# over65()

def peopleChange():
    # Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015
    peopleØ = []
    peopleV = []

    østerbro = data[data[:, 1] == 2]
    vesterbro = data[data[:, 1] == 4]
    for year in range(1992, 2016):
        # 2 == østerbro
        # 4 == vesterbro
        # AAR,BYDEL,ALDER,STATKODE,PERSONER
        #   0,    1,    2,       3,       4
        # Så for year where bydel == 2 og 4
        personerØ = østerbro[østerbro[:, 0] == year]
        personerV = vesterbro[vesterbro[:, 0] == year]
        peopleV.append(sum(personerV[:, 4]))
        peopleØ.append(sum(personerØ[:, 4]))
        # print(peopleV)
        # print(peopleØ)

    plt.figure()

    years = range(1992, 2016)

    # First arg is X, second is Y. Then options.
    plt.plot(list(years), list(peopleV), linewidth=5, label="Vesterbro")
    plt.plot(list(years), list(peopleØ), linewidth=5, label="Østerbro")
    plt.legend(loc=3, bbox_to_anchor=(1, 0))

    # Set chart title and label axes.
    plt.title("Change in number of people", fontsize=24)
    plt.xlabel("Years", fontsize=14)
    plt.ylabel("People", fontsize=14)
    #plt.ylim([0, 35])
    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    plt.show()


peopleChange()
