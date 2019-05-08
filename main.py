# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import wordcloud 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen
from crawler import CrawlerListIdeas
from Ideia import Ideia

stopWords = set(stopwords.words("portuguese"))

c = CrawlerListIdeas()
ideias = c.getLinks()
    
s = ScrapyIdea(ideias)
ideias = s.run()
    
texto = ''
for i in ideias:
    texto = texto + i.problema
    
token = word_tokenize(texto)

filtered = []
for t in token:
    if t not in stopWords:
        filtered.append(t)

textoFiltered = ''
for word in filtered:
    textoFiltered += ' '+word+' '
        
wc = wordcloud.WordCloud().generate(textoFiltered)
plt.imshow(wc)
        

