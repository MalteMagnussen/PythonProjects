import bs4
import requests
from tqdm import tqdm


def getPages():

    url = "https://www.dr.dk/radio/programmer?side=1"
    r = requests.get(url)
    r.raise_for_status()

    soup = bs4.BeautifulSoup(r.text, "html.parser")
    pages = soup.findAll("button", {"class": "pagination__item"})

    numberOfPages = pages[-2].getText()

    print(numberOfPages)

    return int(numberOfPages)


def getTitles(soup):
    titles = soup.findAll("h3", {"class": "spot-content__title"})

    print([text.getText() for text in titles])


for page in tqdm(range(1, getPages() + 1)):
    # print("PAGE:{}".format(page))
    url = "https://www.dr.dk/radio/programmer?side={}".format(page)
    r = requests.get(url)
    r.raise_for_status()

    soup = bs4.BeautifulSoup(r.text, "html.parser")
    getTitles(soup)
