# Exercise with pie charts
# Use this dictionary:
import matplotlib.pyplot as plt
data = {'apple': 10, 'banana': 2, 'citrus': 32, 'dragon fruit': 8}
# Create a pie chart showing the distribution of the fruits

# function for formatting labels in pie chart used below


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)
    return my_autopct


# Pie chart
data = {'Eggs': 15, 'Sandwiches': 70, 'Cup nudles': 45, 'Pizza slices': 10}
explode = (0.1, 0, 0, 0)  # offset second slice
# first returned is the containing figure (fig1), then the subplot Axe object(s) (ax1)
fig1, ax1 = plt.subplots()
ax1.pie(data.values(), labels=data.keys(), explode=explode, autopct=lambda p: '{:.2f}%({:.0f})'.format(p, (p/100)*sum(data.values())),
        # autopct=make_autopct(data.values()),
        # autopct='%.1f',
        # autopct= a format string like '%1.2f%%' for showing pct sign and 2 decimals
        shadow=True, startangle=90)
ax1.set_aspect('equal')
# use instead of labels in ax1.pie(...)
ax1.legend(data.keys(), loc='upper right')
# ax1.axis('equal')
# plt.tight_layout()
plt.show()
