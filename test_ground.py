from numpy import sqrt
import scipy.stats
from htmldate import find_date

w1 = [107, 104, 90, 71, 41, 54, 44, 34]
w2 = [138, 92, 84, 40, 103, 42, 38, 44]
dicti = {1: "12", 4:"13", 0:"14"}

w3 = sum([a*b for a, b in zip(w1, w2)])
new_w1 = sum(sqrt([a*a for a in w1]))
new_w2 = sum(sqrt([a*a for a in w2]))

print(new_w1)
print(w3)
print(f"{w3}/({new_w1}*{new_w2})")
{}
#with open("corpus.txt", "r") as corpus:
#    corpus_content = corpus.readlines()
#    re.find("(January|February|March|April|May|June|July|August|September|October|November|December)+\s+\d+\s+,+\s+\d+\s+\d")

with open("urls3.txt", "r", encoding="utf-8") as urles:
    urles = urles.readlines()
    print(urles)
    for url in urles:
        print(find_date(url.rstrip()))
