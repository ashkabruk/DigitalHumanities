from bs4 import BeautifulSoup
import requests
from htmldate import find_date
import re



def datePublished(split):
    date = {}
    article = 0
    for i in range(2):
        with open("urls{f}.txt".format(f=i + 1), "r") as urls:
            urles = urls.readlines()
            for url in urles:
                article += 1
                res = requests.get(url.rstrip())
                html_page = res.content
                soup = BeautifulSoup(html_page, "html.parser")
                try:
                    date[article] = re.sub("T.*", "", soup.find('time', itemprop='datePublished', content=True)['content'])
                except TypeError:
                    date[article] = find_date(url)
    return date