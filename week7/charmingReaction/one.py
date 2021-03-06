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
    """1. Hvor mange brugte biler er der at vælge i mellem"""
    soup = getSoup(baseUrl)
    divs = soup.findAll("div", {"class": "navigator radioNavigator modulePanel"})
    # print("divs: \n", divs)
    small = divs[0].findAll("small")
    # print("Smalls: \n", small)
    cars = small[0].text
    print("Task one: ", "\n    Number of Cars for Sale: ", cars)


# getCarsCount()


def getFords():
    """2. Udskriv alle biler af mærket Ford"""
    url = baseUrl + "/maerke-ford"
    page = "/side-"
    # Example for request: url+page+numberInLoop
    # class="trackClicks a-page-link" data-ga-act="click" data-ga-lbl="paging-number"
    pagesSoup = getSoup(url)
    a = pagesSoup.findAll(
        "a",
        {
            "class": "trackClicks",
            "data-ga-act": "click",
            "data-ga-lbl": "paging-number",
        },
    )
    # print(a[-1])
    filterPages = filter(str.isdigit, a[-1].text)
    numberOfPages = int("".join(filterPages))
    print("Number of Pages: ", numberOfPages)
    for pageNumber in tqdm(range(1, numberOfPages + 1)):
        soup = getSoup(url + page + str(pageNumber))
        cars = soup.findAll("tr", {"class": "dbaListing listing"})
        for car in cars:
            a = car.findAll("a", {"class": "listingLink"})
            print(a[1].text.encode("utf-8"))
            print("\n")


# getFords()


def getExpensiveCars():
    # "3. Åben de 5 dyreste biler med selenium
    # i decending order og vis dem med et bar chart"
    from selenium import webdriver

    waitingTime = 2

    # Open browser.
    browser = webdriver.Firefox()
    # Go to website
    browser.get(baseUrl)
    # Wait for everything to be loaded
    print("PAGE LOADED")
    browser.implicitly_wait(waitingTime)

    def clickSortByPrice(times):
        thead = browser.find_element_by_class_name("sorting")
        # print("\nthead\n", thead.get_attribute("innerHTML"))
        spans = thead.find_elements_by_class_name("human-ref")
        # print("\nSpans\n", spans)
        printSpan = spans[4]
        # print("\nprintSpan\n", printSpan)
        # print("\nShould say 'Pris'\n", printSpan.get_attribute("innerHTML"))
        printSpan.click()
        print("CLICKED PRICE SORTING", times)
        browser.implicitly_wait(waitingTime)
        # print("PROPER ORDER NOW")

    # After this click, is cheapest cars first
    clickSortByPrice("ONCE")

    # After this click, should be most expensive cars first
    clickSortByPrice("TWICE")

    # Nu er "Åben de 5 dyreste biler med selenium
    # i decending order" denne del done.

    # Now I need to print the first 5 cars.
    html = browser.page_source
    soup = bs4.BeautifulSoup(html, "html.parser")
    cars = soup.findAll("tr", {"class": "dbaListing listing"})
    for index in range(0, 5):
        car = cars[index]
        a = car.findAll("a", {"class": "listingLink"})
        print(a[1].text.encode("utf-8"))
        print("\nPRICE: ", a[2].text.encode("utf-8"))
        print(
            "\n_______________________________________________________________________________________\n"
        )


getExpensiveCars()
