from bs4 import BeautifulSoup
import requests
import nltk

def unique(items):
    found = set()
    keep = []
    for item in items:
        if item not in found:
            found.add(item)
            keep.append(item)
    return keep

with open("urls.txt", "r+") as urls:
    urls_content = urls.readlines()
    for i in unique(urls_content):
        urls.seek(0)
        urls.write("\n" + i.rstrip() + "\n")
        urls.truncate()