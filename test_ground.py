from numpy import sqrt
import re
import scipy.stats

w1 = [107, 104, 90, 71, 41, 54, 44, 34]
w2 = [138, 92, 84, 40, 103, 42, 38, 44]

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

print(scipy.stats.norm.ppf(0.995))
