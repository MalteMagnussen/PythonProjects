# Charming Reaction
# Link	https://www.dba.dk/biler/biler/
# "1. Hvor mange brugte biler er der at vælge i mellem"
# "2. Udskriv alle biler af mærket Ford"
# "3. Åben de 5 dyreste biler med selenium
# i decending order og vis dem med et bar chart"

import bs4
import requests
from tqdm import tqdm

baseUrl = "https://www.dba.dk/biler/biler"


def getSoup(url):
    r = requests.get(
        url,
        headers={
            "User-Agent": "My User Agent 1.0",
            "From": "youremail@domain.com",  # This is another valid field
        },
    )
    r.raise_for_status()

    soup = bs4.BeautifulSoup(r.text, "html.parser")

    # with open(url) as f:
    #     example_html = f.read()

    # soup = bs4.BeautifulSoup(example_html, "html.parser")

    return soup


def getCarsCount():
    soup = getSoup(baseUrl)
    divs = soup.findAll("div", {"class": "navigator radioNavigator modulePanel"})
    # print("divs: \n", divs)
    small = divs[0].findAll("small")
    # print("Smalls: \n", small)
    cars = small[0].text
    print("Task one: ", "\n    Number of Cars for Sale: ", cars)


getCarsCount()
