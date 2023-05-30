from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")

bs = BeautifulSoup(html.read(), "html.parser")

name_list = bs.find_all("span", {"class": "green"}, limit=10)  # Limited to top 10
x_list = bs.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])  # Multiple tag names
y_list = bs.find_all("span", {"class": ["green", "red"]})  # Multiple class attributes

for name in name_list:
    print(name.get_text())

prince = bs.find_all(string="the prince")
print(len(prince))
