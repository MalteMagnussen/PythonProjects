import matplotlib.pyplot as plt

# Class exercise
# with the following dataset:

student_attendance = {'day1': 33, 'day2': 34, 'day3': 29,
                      'day4': 31, 'day5': 28, 'day6': 26, 'day7': 30}

# create a line graph showing attendance over time. hint: use keys() and values() method of the dictionary.
# add title and labels for x and y axis.

plt.figure()

# First arg is X, second is Y. Then options.
plt.plot(list(student_attendance.keys()), list(
    student_attendance.values()), linewidth=5)

# Set chart title and label axes.
plt.title("Attendance over time.", fontsize=24)
plt.xlabel("Days", fontsize=14)
plt.ylabel("Attendance", fontsize=14)
#plt.ylim([0, 35])
# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Save as image
plt.savefig('PythonProjects/week3/plotting/attendance.png',
            bbox_inches='tight')

plt.show()
