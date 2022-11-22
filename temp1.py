import requests
from bs4 import BeautifulSoup
import pandas as pd
# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get('https://www.basketball-reference.com')

# searchBox = driver.find_element_by_xpath(
#     '//*[@id = "header"]/div[3]/form/div/div/input[2]')
# searchBox.send_keys('Boston Celtics')
# searchButton = driver.find_element_by_xpath(
#     '//*[@id="header"]/div[3]/form/input[1]')
# searchButton.click()
# result = driver.find_element_by_xpath(
#     '//*[@id="teams"]/div[1]/div[1]/strong/a')
# result.click()

# url = driver.current_url
url = "https://www.basketball-reference.com/players/p/poolejo01.html"

htmlContent = requests.get(url).content

soup = BeautifulSoup(htmlContent, 'html.parser')

perGame = soup.find(id="per_game")

headers = [i.getText() for i in perGame.find(
    'thead').find('tr').findAll('th')][1:]
print(headers)
rows = []
for i in range(len(perGame.find('tbody').findAll('tr'))):
    rows.append([i.getText()
                 for i in perGame.find('tbody').findAll('tr')[i].findAll('td')])
print(rows)
print([i.getText() for i in perGame.find('tfoot').find('tr').findAll('td')])

# tempCSV = pd.DataFrame(rows, columns=headers)

# tempCSV.to_csv("tempCSV.csv", index=False)
