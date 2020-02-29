import os.path
import pandas as pd
import requests
import zipfile


if os.path.isfile('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_800760.zip'):
    print("File exist")
else:
    print("File not exist")
    print("Fetching zip file from world bank")
    # url = 'http://api.worldbank.org/v2/en/country/DNK;URY'
    # response = requests.get(url, params={'downloadformat': 'csv'})
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?lang=en&delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=*&ALDER=*&CIVILSTAND=F%2CTOT&Tid=*'
    response = requests.get(url)

    # print(response.headers)

    # get the filename
    fname = response.headers['Content-Disposition'].split('=')[1]

    # write content to file (zip file writing bytes)
    if response.ok:  # status_code == 200:
        with open(fname, 'wb') as f:
            f.write(response.content)
    print('-----------------')
    print('Downloaded {}'.format(fname))

    # extract content of zip file in current folder
    zipfile.ZipFile(fname, 'r').extractall('.')


try:
    # Read CSV
    data = pd.read_csv(
        'API_EN.ATM.CO2E.KT_DS2_en_csv_v2_800760.csv', skiprows=4)
    columns_names = data.columns
    # print('column names:\n', list(columns_names), '\n\n')
    countries = data['Country Name']
    # print("{} countries are in the dataset.".format(len(countries)))
    # print('countries are of data type: ', type(countries))
    # print(list(countries))
    # Create a new pandas Series with countries as labels and a random number as values
    import random
    # random.sample takes a population and a sample size k and returns k random members of the population.
    random_val_pr_country = pd.Series(random.sample(
        range(1, len(countries)+1), len(countries)), index=countries)
    print(random_val_pr_country.sort_values())
except:
    print("File not found")

# instansiate Series from dict
# new_series = pd.Series(dict({'a':3,'b':6,'c':9}))
# print(new_series)
