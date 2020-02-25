import requests

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
