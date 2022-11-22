import csv
from selenium import webdriver
driver = webdriver.Firefox()

URL = "https://www.basketball-reference.com/search/search.fcgi?search="
urls = []
count = 1

# below block of code will read lines from players name and open in firefox then we store the url in a list

with open("/home/jayesh/Documents/Programming/RP1/PlayerName/Pre.txt") as pt:
    lines = pt.readlines()
    for i in lines:
        driver.get(URL+i)
        if "search" in driver.current_url:
            urls.append(driver.find_element_by_class_name(
                "search-item-url").text)
        else:
            temp = driver.current_url
            index = temp.index("/players")
            urls.append(temp[index:])
        print(count)
        count += 1

print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")
print("DONE!!!!!!! now writing in csv")


# below block of code will write csv data to the file with url and name of the players


fields = ["Name", "URL"]
count = 1
with open("/home/jayesh/Documents/Programming/RP1/PlayerName/Pre.txt") as pt, open("/home/jayesh/Documents/Programming/RP1/PlayerName/pre.csv", 'w', newline='') as cs:
    lines = pt.readlines()
    csvWriter = csv.writer(cs)
    csvWriter.writerow(fields)
    n = len(urls)
    for i in range(n):
        csvWriter.writerow([lines[i].strip(), urls[i]])
        print(count)
        count += 1
