# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from Ideia import Ideia
import time

class CrawlerListIdeas():
    
    def __init__(self):
        self.urlRoot = 'http://pr1.sinapsedainovacao.com.br'
        self.urlCategoria = 'http://pr1.sinapsedainovacao.com.br'
        #self.urlCategoria = 'http://pr1.sinapsedainovacao.com.br/ideias/saude-e-bem-estar'
        self.currentPage = ''
        self.ideias = []
        self.tagNameListIdeas = 'list-ideas-inner'
        self.qtdePaginas = 1
        
    def getBrowser(self, link):
        browser = webdriver.Chrome(executable_path='chromedriver.exe')
        browser.get(link)
        
        return browser
        
    def getBrowserElementPresent(self, link, element):        
        browser = self.getBrowser(link)                
        element_present = EC.presence_of_element_located((By.CLASS_NAME, element))
        WebDriverWait(browser, 5).until(element_present)
        return  browser
    
    def clickButtonNextPage(self, browser):        
        button = browser.find_element_by_css_selector('li.next > a.step')
        button.click()    
        time.sleep(1.5)
        return browser
    
    def getLinks(self, page):        
        soup = BeautifulSoup(page, 'html.parser')        
        div = soup.find_all("div", attrs={"class": "list-ideas-inner"})     

        for p in div:            
            for index, child in enumerate(p.findChildren('a')): 
                if 'class' in child.attrs:                               
                    if 'media' in child['class']:
                        urlIdeia = self.urlRoot + child['href'] 
                        print(urlIdeia)
                        self.ideias.append(Ideia(urlIdeia))
        
        return self.ideias    
    
    
    def run(self):        
        for i in range(self.qtdePaginas):
            if self.currentPage == '':
                self.currentPage = self.urlCategoria
                browser = self.getBrowserElementPresent(self.currentPage, self.tagNameListIdeas)
            else:
                browser = self.clickButtonNextPage(browser)
            self.getLinks(browser.page_source)   
            
        return self.ideias
        
        

    
class ScrapyIdea():
    
    def __init__(self, ideias):
        self.ideias = ideias
        
    def getHtmlPage(self, link):
        page = urlopen(link).read()
        return page
        
    def run(self):
        for ideia in self.ideias:
            page = self.getHtmlPage(ideia.link)            
            soup = BeautifulSoup(page, 'html.parser')
            div = soup.findAll("div", {"class": "content"})        
            for p in div:    
                for index, child in enumerate(p.findChildren()):
                    if child.get_text() == 'Descrição do problema':                    
                        texto = p.findChildren()[index+1].get_text()
                        ideia.problema = texto.strip()
                        
                    if child.get_text() == 'Solução Proposta':                    
                        texto = p.findChildren()[index+1].get_text()
                        ideia.proposta = texto.strip()  
                        break
        return self.ideias
    
            
if __name__ == '__main__':
    c = CrawlerListIdeas()
    ideias = c.run()
    print(ideias)
    '''
    s = ScrapyIdea(ideias)
    ideias = s.run()
    
    for i in ideias:
        print('----problema----')
        print(i.problema)
        
        print('----proposta----')
        print(i.proposta)
'''
    
    
    