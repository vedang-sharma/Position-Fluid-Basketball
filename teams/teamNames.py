import requests
from bs4 import BeautifulSoup

url = "https://www.basketball-reference.com/teams/"

htmlContent = requests.get(url).content
soup = BeautifulSoup(htmlContent, 'html.parser')


allTeams = [i.find('th').getText()
            for i in soup.findAll('tr', class_='full_table')]

activeFranchises = allTeams[:30]
defunctFranchises = allTeams[30:]

print(defunctFranchises)
