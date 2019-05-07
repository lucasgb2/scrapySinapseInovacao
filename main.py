# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import wordcloud 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen

html = urlopen("http://pr1.sinapsedainovacao.com.br/pr1/ideia/plataforma-que-aumenta-a-felicidade-e-performance-do-profissional")     
soup = BeautifulSoup(html.read(), 'html.parser')
div = soup.findAll("div", {"class": "content"})        
for p in div:    
    for index, child in enumerate(p.findChildren()):
        if child.get_text() == 'Solução Proposta':                    
            texto = p.findChildren()[index+1].get_text()
            print(texto)
            

stopWords = set(stopwords.words("portuguese"))

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
        

    