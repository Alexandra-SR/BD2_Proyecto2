import os
import json
import errno
import nltk
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
import math
import re

input_directory = "dataset_clean"
curpath = os.path.abspath(os.curdir)
punc = [ "¡", "«", "»", ".", ",", ";", "(", ")", ":", "@", "RT", "#", "|", "¿", "?", "!", "https", "$", "%", "&", "'", "''", "..", "...", '\'', '\"' ]
#punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~«»'''
with open('stoplist.txt') as file:
    stoplist = [line.lower().strip() for line in file]
stoplist += ["«", "»", ".", ",", ";", "(", ")", ":", "@", "RT", "#", "|", "?", "!", "https", "$", "%", "&", "'", "''", "..", "...", '\'', '\"' ]
archivos = os.listdir(input_directory)
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
    for filename in archivos[:5]:
        lista = []
        if filename.endswith(".json") : 
            with open(input_directory + '\\' + filename, 'r', encoding='utf-8') as all_tweets:
                all_tweets_dictionary = json.load(all_tweets)
                for tweet in all_tweets_dictionary:
                    temp = readFile(all_tweets_dictionary[tweet])
                    lista.append(temp)
                tf.append(merge(lista))
   
    tfidf(tf)
  
      
def tfidf(tf):
    lista = {}
    it = 0
    for i in tf:
        for k in i:
            wtfidf = math.log(1 + i[k]) * math.log(len(tf)/df(k, tf))
            if k in lista:
                lista[k] = str(lista[k]) + "," + str(archivos[it]) + ":" + str(wtfidf)             
            else:
                lista[k] = str(archivos[it]) + ":" + str(wtfidf)
        it += 1
        
    it1 = 0
    for i in lista:
        print(i, lista[i])
        print('\n')
        it1 += 1
        if it1 == 5: break
    return lista

def df(word, lista):
    c = 0
    for i in lista:
        if word in i:
            c += 1
    return c

def remove_URL(sample):
    return re.sub(r"http\S+", "", sample)

def readFile(name):
    ans = []
    stemmer = SnowballStemmer('spanish')
    palabras = nltk.word_tokenize(remove_URL(signosp(name.lower()))) 
    for token in palabras:
        #w1 = signosp(token)
        word = stemmer.stem(token)
        if word not in stoplist:
            ans.append(word)
    return Counter(ans)

print(json_tweets_to_dic())


