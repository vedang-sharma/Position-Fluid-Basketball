from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/players/d/doncilu01.html"

html = urlopen(url)
soup = BeautifulSoup(html, features="lxml")

print(soup.findAll('thead/tr'))

# headers = [th.getText() for th in soup.findAll('tr')[17].findAll('th')]
# print(headers)

# rows = soup.findAll('tr')[1:]
# rows_data = [[td.getText() for td in rows[i].findAll('td')]
#              for i in range(len(rows))]
# rows_data = rows_data[:3]
# last_year = 2020
# for i in range(0, len(rows_data)):
#     rows_data[i].insert(0, last_year)
#     last_year -= 1

# # for i in rows_data:
# #     print(i)

# nba_finals = pd.DataFrame(rows_data, columns=headers)

# nba_finals.to_csv("nba_finals_history.csv", index=False)
