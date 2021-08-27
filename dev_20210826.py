# Web scrapping.

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

#print(soup.find(id='score_28306390'))

story = soup.select('.storylink')
score = soup.select('.score')
#print(score[0])

links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_list(links, subtext):
    custom_list = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                custom_list.append({'title': title, 'link': href, 'votes': points})
    return custom_list


print(create_custom_list(links, subtext))