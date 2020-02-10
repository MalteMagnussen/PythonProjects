# Class exercise¶
# 1.1 Using this dict:
import matplotlib.pyplot as plt
data = {'Holger': 25, 'Helga': 54, 'Hasse': 76,
        'Halvor': 12, 'Hassan': 43, 'Hulda': 31, 'Hansi': 102}
# display a bar plot of the people and there ages sorted by age.
# 1.2 Add title and x and y axis labels to the bar plot

# 2.1 Using the kkdata module with population data from Copenhagen display a
# line graph showing the population development over time (year on x and population on y)

plt.figure()

# First arg is X, second is Y. Then options.
plt.bar(list(data.keys()), list(
    data.values()), linewidth=5)

# Set chart title and label axes.
plt.title("People and their ages.", fontsize=24)
plt.xlabel("Age", fontsize=14)
plt.ylabel("People", fontsize=14)
#plt.ylim([0, 35])
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Save as image
plt.savefig('PythonProjects/week3/plotting/ages01.png',
            bbox_inches='tight')

plt.show()
