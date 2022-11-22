from sys import implementation
from bs4 import BeautifulSoup
import requests

pre_2015 = set()
post_2015 = set()


def player_list(team):

    url = 'https://www.basketball-reference.com'

    for i in team:
        for j in i:
            print(url + j[0])
            data = requests.get(url + j[0])
            data = BeautifulSoup(data.text, 'html.parser')

            ros = data.tbody
            ros = ros.find_all('td', {'data-stat': 'player'})

            for it in ros:
                pre_2015.add(it.string)

            for k in j[2:6]:

                base = url + str(k)
                print(base)
                data = requests.get(url + str(k))
                data = BeautifulSoup(data.text, 'html.parser')

                ros = data.tbody
                ros = ros.find_all('td', {'data-stat': 'player'})

                for it in ros:
                    post_2015.add(it.string)

            for k in j[7:]:

                base = url + str(k)
                print(base)

                data = requests.get(base)
                data = BeautifulSoup(data.text, 'html.parser')

                ros = data.tbody
                ros = ros.find_all('td', {'data-stat': 'player'})

                for it in ros:
                    pre_2015.add(it.string)


def player_name(url, tn):

    yl = list()

    for i in tn:

        t_url = url + i

        data = requests.get(t_url)
        data = BeautifulSoup(data.text, 'html.parser')

        pn = data.tbody.find_all('tr')

        res = list()

        for i in pn:
            res.append(i.a['href'])

        yl.append(res[1:13])

    return yl


def team_url(url):

    url = url + '/teams/'

    data = requests.get(url)
    data = BeautifulSoup(data.text, 'html.parser')

    tn = data.find(id='teams_active')
    tu = list()

    tn = tn.tbody.find_all(class_='full_table')

    for i in tn:
        tu.append(i.a['href'])

    res = list()
    res.append(player_name('https://www.basketball-reference.com', tu))

    player_list(res)


def main():

    base_url = 'https://www.basketball-reference.com'

    team_url(base_url)

    # pre2015 = list(pre_2015)
    # post2015 = list(post_2015)

    # for i in pre_2015:
    #     print(i)
    with open('Pre.txt', 'w') as file_obj:
        for i in pre_2015:
            file_obj.write(str(i) + '\n')

    with open('Post.txt', 'w') as file_obj:
        for i in post_2015:
            file_obj.write(str(i) + '\n')


if __name__ == '__main__':
    main()
