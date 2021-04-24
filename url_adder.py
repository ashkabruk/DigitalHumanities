from bs4 import BeautifulSoup
import requests
import nltk
from htmldate import find_date

date = {}
article = 0

for i in range(2):
    with open("urls{f}.txt".format(f=i+1), "r") as urls:
        with open("cleaned_corpus.txt", "a", encoding="utf-8") as corpus:
            urles = urls.readlines()
            for url in urles:
                article += 1
                res = requests.get(url.rstrip())
                html_page = res.content
                soup = BeautifulSoup(html_page, "html.parser")
                try:
                    date[article] = soup.find('time', itemprop='datePublished', content=True)['content']
                except TypeError:
                    date[article] = find_date(url)
                webtext = soup.find_all(text=True)
                output = ''
                for s in soup.select('section'):
                    s.extract()
                blacklist = [
                        '[document]',
                        'noscript',
                        'header',
                        'html',
                        'meta',
                        'head',
                        'input',
                        'script',
                        'span',
                        'ol',
                        'menu',
                        'nav',
                        'li',
                        'footer',
                        'a',
                        'fieldset',
                        'option',
                        'div',
                        'style',
                        'link',
                        'form',
                        'legend',
                        'i',
                        'button',
                        'title',
                        'footer',
                        'img',
                        'section'
                    ]
                for t in webtext:
                    if t.parent.name not in blacklist:
                        output += '{} '.format(t)
                output = nltk.word_tokenize(output)
                check = ""
                for i in output:
                    check += i + " "
                corpus.write(check + "\n")