from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), "html.parser")
        tittle = bs.body.h1
    except AttributeError as e:
        return None

    return tittle


tittle = get_title("https://www.pythonscraping.com/pages/page1.html")

if tittle is None:
    print("Tittle could be not be found.")
else:
    print(tittle)
