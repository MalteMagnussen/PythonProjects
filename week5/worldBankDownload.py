import zipfile
import requests
import pandas as pd
import os.path


if os.path.isfile('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_800760.zip'):
    print("File exist")
else:
    print("File not exist")
    print("Fetching zip file from world bank")
    # url = 'http://api.worldbank.org/v2/en/country/DNK;URY'
    # response = requests.get(url, params={'downloadformat': 'csv'})
    url = 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv'
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
    print('column names:\n', list(columns_names), '\n\n')
    countries = data['Country Name']
    print("{} countries are in the dataset.".format(len(countries)))
    print('countries are of data type: ', type(countries))
    print(list(countries))
except:
    print("File not found")
