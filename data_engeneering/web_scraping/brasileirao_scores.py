import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

today = date.today()

url = "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/"

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

full_names = soup.find_all("div", class_="visible-sm visible-lg")

team_scores = soup.find("tbody", class_="score")
row_scores = team_scores.find_all("tr")

main_table = []

cont = 0
while cont < len(full_names) - 2:
    for scores in row_scores:
        team_table = [full_names[cont].text]
        each_score = scores.find_all("td")
        for score in each_score:
            team_table.append(score.text)
        main_table.append(team_table)
        cont += 1

with open(f"tabela_brasileirao_{today}.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    for team in main_table:
        writer.writerow(team)
