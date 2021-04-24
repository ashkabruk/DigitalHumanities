from nltk.tokenize import RegexpTokenizer
from scipy import spatial
import nltk
import collections
import re
from typing import List, Tuple
from datePublished import split_dates

test = "China ’ s crackdown on cryptocurrency trading – a sign of things to come Edition Search An illustration photo of Bitcoin ( virtual currency ) coins China ’ s crackdown on cryptocurrency trading – a sign of things to come September 20 , 2017 8.26am BST The University of Melbourne Author DIRECTOR OF STUDIES , BANKING AND FINANCE LAW , The University of Melbourne Disclosure statement Partners provides funding as a founding partner of The Conversation AU . The Conversation UK receives funding from these organisations View the full list The decision to order several Bitcoin and other cryptocurrencies exchanges to close shows how much of a they are perceived to be to financial stability and social order in China . The decision to also ban initial coin offerings altogether ( the unregulated means by which funds are raised for a new cryptocurrency venture ) has taken traders and analysts by surprise . China is the world ’ s cryptocurrency market with around 80 % of Bitcoin transactions taking place in yuan . The ( a digital ledger in which digital currency transactions are publicly recorded ) is poised to have a on the future of finance . This recent crackdown suggests the Chinese government is determined to cement its place as a leading rule maker and power-broker in the quickly emerging area of cryptocurrency transactions and exchange . Chinese relationship with bitcoin The Chinese government released a of 60 initial coin offering trading platforms and instructed local agencies to make sure all platforms were listed and closed down . The delayed crackdown is in line with previous practice in China . The Chinese government often adopts a wait-and-see approach to activities that are largely unregulated until the magnitude of the activity becomes clear . The extent of speculative investment and the risk of losses to investors if the bubble bursts motivated the government to intervene in cryptocurrency trading . Read more : In China , the popularity of cryptocurrencies has been boosted by the of controls on money moving out of the country over the past two years . This has lowered the value of the China ’ s currency , the renminbi , as investors seek assets in different denominations and chase higher yields . Cryptocurrencies are also popular because they can be used to transfer funds offshore and circumvent foreign exchange controls . The government is with the of cryptocurrencies and initial coin offerings to perpetrate and disguise fraudulent activity , including money laundering and ponzi type investment schemes . Chinese authorities are anxious to avoid any social unrest in the lead-up to the 19th Party Congress . The effects of the , where the A-share market lost one-third of its value over a period of one month , are still being felt . In some respects , the regulatory intervention in China is mirrored in other countries that have been dragging their heels in coming to terms with cryptocurrencies . It was only in July this year that the US Securities Commission issued a determining that DAO tokens were “ securities ” and must be regulated accordingly . China ’ s own cryptocurrency In January last year , the People ’ s Bank of China issued a notice announcing it would be issuing its own of the renminbi . The notice highlighted the benefits of a government backed digital currency in terms of cost , coverage , convenience and security . Read more : In the initial phase , it ’ s likely that trading in this digital currency will be limited to regulated entities such as banks along similar lines to trading on the conventional foreign exchange markets . By launching its own digital currency , the Chinese government avoids the risks associated with privately-issued cryptocurrencies and ensuring they are not used as a means of circumventing China ’ s strict capital and currency controls . When China introduces its own digital currency ( no formal date has yet been announced ) , the impact on the global economy will be significant . Not only will it challenge the existing global payment systems and establish China as a leading rule maker in this area , it will also enhance the importance of the renminbi as a global reserve currency . Events"

def context_window(text, context=5, top=8):
    word1 = input("First word: ")
    word2 = input("Second word: ")
    num_w1 = 0
    num_w2 = 0
    c = [0 for x in range(9)]
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    counter = collections.Counter(tokens)
    most_common = counter.most_common(top)
    most_list = []
    x, y = 0, 0
    for i in most_common:   #Unnests most_common
        most_list.append(most_common[x][y])
        x += 1
    w = {word1: dict(zip(most_list, c)), word2: dict(zip(most_list, c))}
    try:    #IndexError if it's longer or shorter than the list
        for i, word in enumerate(tokens):
            if word == word1:
                num_w1 += 1
            if word == word2:
                num_w2 += 1
            if word in w.keys():
                for j in range(-context, context+1):    #Goes through 5 words before and after the vector words
                    if tokens[i+j] in most_list:    #Checks whether the top words are in the context window and adds +1 if the case
                        w[word][tokens[i+j]] += 1
    except IndexError:
        pass
    print(w)
    w1 = list(w[word1].values())
    w2 = list(w[word2].values())
    sentence = "Hits '" + word1 + "': " + str(num_w1) + "\n" + "Hits '" + word2 + "': " + str(num_w2) + "\n" + "Hits in context window of length " + str(context) + ": " + str(w1[1])
    print(sentence)
    return "Cosine similarity: " + str(1 - spatial.distance.cosine(w1, w2))

def top_words(top, pos_tags: List[str], text):
    tokens = nltk.pos_tag(RegexpTokenizer(r'\w+').tokenize(text))
    top_words = []
    for element in tokens:
        (word, coord) = element
        if coord in pos_tags:
            top_words.append(word)
        else:
            continue
    counter = collections.Counter(top_words)
    most_common = counter.most_common(top)
    print(most_common)

if __name__ == '__main__':
    pass

#with open("cleaned_corpus.txt", "r", encoding="utf-8") as corpus:
#    corpus_content = corpus.read()
#    word_list = corpus_content.split()
#    print(len(word_list))
#    top_words(30, ["VB"], corpus_content)
#    print(context_window(corpus_content))

with open("cleaned_corpus.txt", "r", encoding="utf-8") as corpus:
    int1, int2 = split_dates()
    corpus_content1 = ""
    corpus_content2 = ""
    for i in int1:
        corpus_lines1 = corpus.readlines(i)
        for a in corpus_lines1:
            corpus_content1 += a
    for i in int2:
        corpus_lines2 = corpus.readlines(i)
        for a in corpus_lines2:
            corpus_content2 += a
    top_words(30, ["NN", "NNS", "NNP", "NNPS"], corpus_content1)
    top_words(30, ["NN", "NNS", "NNP", "NNPS"], corpus_content2)

