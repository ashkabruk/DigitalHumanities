from bs4 import BeautifulSoup
import requests
from htmldate import find_date
import re
import operator
from date_urls import date



def date_published():
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
    with open("date_urls.txt", "w+", encoding="utf-8")as dates:
        dates.write(str(date))

def split_dates():
    split = input("Date for split in format YYYY-MM-DD: ")
    date[0] = str(split)
    sorted_tuples = sorted(date.items(), key=operator.itemgetter(1))
    sorted_date = {k: v for k, v in sorted_tuples}
    dicti = sorted_date.keys()
    for i, datum in enumerate(sorted_date.values()):
        if datum == split:
            dict1 = list(dicti)[:i]
            dict2 = list(dicti)[i+1:]
        else:
            continue
    return dict1, dict2