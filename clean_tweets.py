import os
import json
import errno
import nltk
from nltk.stem.snowball import SnowballStemmer
from collections import Counter

input_directory = "dataset_clean"
curpath = os.path.abspath(os.curdir)
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~«»'''

with open('stoplist.txt') as file:
    stoplist = [line.lower().strip() for line in file]
stoplist += ['.', '?', '-', ';', ':', ',', '\'', '\"', '!', '¿', '¡', '»', '(', ')', '«', '@', '#']

def signosp(word):
    for x in word:
        if x in punc:
            word = word.replace(x, "")
    return word

def merge(lista):
    ans = Counter()
    for i in lista:
        ans += i
    return ans

def json_tweets_to_dic():
    tf = []
    for filename in os.listdir(input_directory):
        lista = []
        if filename.endswith(".json") : 
            with open(input_directory + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
                all_tweets_dictionary = json.load(all_tweets)
                for tweet in all_tweets_dictionary:
                    temp = readFile(all_tweets_dictionary[tweet])
                    lista.append(temp)
                tf.append(merge(lista))
        break                  



def readFile(name):
    ans = []
    stemmer = SnowballStemmer('spanish')
    palabras = nltk.word_tokenize(signosp(name.lower())) 
    for token in palabras:
        #w1 = signosp(token)
        word = stemmer.stem(token)
        if word not in stoplist:
            ans.append(word)
    return Counter(ans)

print(json_tweets_to_dic())


