from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import json
from datetime import date

url = "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/"

option = Options()
option.add_argument('--headless')
driver = webdriver.Chrome()

driver.get(url)
driver.implicitly_wait(1)

element = driver.find_element(By.CLASS_NAME, "app__container")
html_content = element.get_attribute("outerHTML")

column_names = ["POS", "TIME"]

soup = BeautifulSoup(html_content, "html.parser")

stats_header = soup.find("thead", {"class": "score"}).find_all("td", limit=9)
for stat_name in stats_header:
    stat = stat_name.text
    column_names.append(stat)

team_stats_row = []

team_position = soup.find_all("span", {"class": "position ng-binding"})
for position in team_position:
    team_position_table = [position.text]
    team_stats_row.append(team_position_table)

team_name = soup.find_all("div", {"class": "visible-sm visible-lg ng-binding"})
for n, team in enumerate(team_name):
    team_stats_row[n].append(team.text)

table_stats = soup.find("tbody", {"class": "score"}).find_all("tr", {"class": "ng-scope"})
for n, stats_row in enumerate(table_stats):
    team_stats = stats_row.find_all("td", limit=9)
    for stat in team_stats:
        team_stats_row[n].append(stat.text)

driver.quit()

df = pd.DataFrame(np.array(team_stats_row), columns=column_names)

print(df.to_string(index=False))
