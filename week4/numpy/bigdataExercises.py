# Exercise numpy and csv
# 1. load the csv file: befkbhalderstatkode.csv into a numpy ndarray
import numpy as np
import countryCodes
filename = './befkbhalderstatkode.csv'

data = np.genfromtxt(
    filename, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave',
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst',
          10: 'Amager Vest', 99: 'Udenfor'}

# AAR,BYDEL,ALDER,STATKODE,PERSONER

# 2. How many german children were 0 years old in 2015?
print(countryCodes.country_codes[5180])
# 2 third column X == 0
# 0 first column X == 2015
mask = ((data[:, 0] == 2015) & (data[:, 2] == 0))
kids = data[mask]
print("Number of german kids 0 years old in 2015:", sum(kids[4]))  # 7140


def populationData(AAR=None, BYDEL=None, ALDER=None, STATKODE=None):
    # 3. create a function that can take any combination of the 4 parameters:AAR,BYDEL,ALDER,STATKODE and return population data

    pass

# 4. create a new function like previous so that it can sum values for all ages if age is not provided to the function
# 5. further add functionality to sum values if citizenship or area was not provided to function.
# 6. create a new function that can also give average values for each year if year whas not provided.
# 7. create a function, that given year and nationality can return which area had the most of these nationals by that year.
#       Test it by finding out which area had the most Moroccan people in both 1992 and 2015
# 8. Find the Area(s) where fewest foreingers lived in Copenhagen in 1992 and 2015 respectively
# 9. Find out what age most French people have in 2015

# AAR,BYDEL,ALDER,STATKODE,PERSONER
