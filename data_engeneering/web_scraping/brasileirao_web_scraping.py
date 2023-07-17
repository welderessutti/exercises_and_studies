from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import json
from datetime import date


def get_html_content(target_url):
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Chrome()

    driver.get(target_url)
    driver.implicitly_wait(1)

    element = driver.find_element(By.CLASS_NAME, "app__container")
    html_content_ = element.get_attribute("outerHTML")

    driver.quit()

    return html_content_


def create_soup(html_content_):
    soup_ = BeautifulSoup(html_content_, "html.parser")

    return soup_


def get_table_headers(soup_):
    column_names = ["POS", "TIME"]
    stats_header = soup_.find("thead", {"class": "score"}).find_all("td", limit=9)
    for stat_name in stats_header:
        stat = stat_name.text
        column_names.append(stat)

    return column_names


def get_team_position(soup_):
    team_stats_row = []
    team_position = soup_.find_all("span", {"class": "position ng-binding"})
    for position in team_position:
        team_position_table = [position.text]
        team_stats_row.append(team_position_table)

    return team_stats_row


def get_team_name(soup_, team_stats_row):
    team_name = soup_.find_all("div", {"class": "visible-sm visible-lg ng-binding"})
    for n, team in enumerate(team_name):
        team_stats_row[n].append(team.text)

    return team_stats_row


def get_team_stats(soup_, team_stats_row):
    table_stats = soup_.find("tbody", {"class": "score"}).find_all("tr", {"class": "ng-scope"})
    for n, stats_row in enumerate(table_stats):
        team_stats = stats_row.find_all("td", limit=9)
        for stat in team_stats:
            team_stats_row[n].append(stat.text)

    return team_stats_row


def create_dict(stats_, headers_):
    df = pd.DataFrame(np.array(stats_), columns=headers_)
    print(df.to_string(index=False))

    brasileirao_dict_ = {"brasileirao": df.to_dict("records")}
    print(brasileirao_dict_)

    return brasileirao_dict_


def create_json_file(brasileirao_dict_):
    today = date.today()
    js = json.dumps(brasileirao_dict_, indent=4)
    with open(f"classificacao_{today}.json", "w", encoding="utf-8") as file:
        file.write(js)


url = "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/"

html_content = get_html_content(url)

soup = create_soup(html_content)

headers = get_table_headers(soup)

positions = get_team_position(soup)

names = get_team_name(soup, positions)

stats = get_team_stats(soup, names)

brasileirao_dict = create_dict(stats, headers)

create_json_file(brasileirao_dict)
