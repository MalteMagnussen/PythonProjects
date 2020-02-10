import matplotlib.pyplot as plt

plt.figure()
input_values = range(1, 6)
squares = [x ** 2 for x in input_values]

plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Set size of tick labels.

plt.tick_params(axis='both', labelsize=14)
plt.savefig('PythonProjects/week3/plotting/foo.png', bbox_inches='tight')
