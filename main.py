# -*- coding: utf-8 -*-
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import wordcloud 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from urllib.request import urlopen
from crawler import CrawlerListIdeas, ScrapyIdea
from Ideia import Ideia

stopWords = set(stopwords.words("portuguese"))



def getScrapyIdeias():
    c = CrawlerListIdeas()
    ideias = c.run()
    
    s = ScrapyIdea(ideias)
    ideias = s.run()    
    
    return ideias


def getTextoProblema(ideias):
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
    
    return textoFiltered            
    

def getTextoProposta(ideias):
    texto = ''
    for i in ideias:
        texto = texto + i.proposta
        
    token = word_tokenize(texto)
    
    filtered = []
    for t in token:
        if t not in stopWords:
            filtered.append(t)    
    
    textoFiltered = ''
    for word in filtered:
        textoFiltered += ' '+word+' '    
    
    return textoFiltered    



ideias = getScrapyIdeias()

texto =  getTextoProblema(ideias)       
print(texto)
wc = wordcloud.WordCloud().generate(texto)
plt.imshow(wc)

wc = wordcloud.WordCloud().generate(getTextoProposta(ideias))
plt.imshow(wc)
        

