# -*- coding: utf-8 -*-

class Ideia():
    def __init__(self, link):
        self.link = link
        self.problema = ''
        self.proposta = ''
        
    def __repr__(self):
        print('Link: %s \n Descrição da proposta: %s' % (self.link, self.proposta))

