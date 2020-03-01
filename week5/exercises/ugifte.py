import os.path
import pandas as pd
import requests
import zipfile

filename = 'FOLK1A.csv'

if os.path.isfile(filename):
    print("File exist")
else:
    print("File not exist")
    print("Fetching csv from api.statbank.dk")
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F%2CTOT&Tid=*'
    response = requests.get(url, params={'downloadformat': 'csv'})

    print("Headers:", response.headers)

    # get the filename
    fname = response.headers['Content-Disposition'].split('=')[1]
    filename = fname
    print("Filename:", fname)

    # write content to file (zip file writing bytes)
    if response.ok:  # status_code == 200:
        with open(fname, 'wb') as f:
            f.write(response.content)
    print('-----------------')
    print('Downloaded {}'.format(fname))

    # extract content of zip file in current folder
    # zipfile.ZipFile(fname, 'r').extractall('.')


try:
    # Read CSV
    data = pd.read_csv(
        filename, skiprows=1)


except:
    print("File not found")
