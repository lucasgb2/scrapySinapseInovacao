# -*- coding: utf-8 -*-

class Ideia():
    def __init__(self, link):
        self.link = link
        self.problema = ''
        self.proposta = ''
        
    def __repr__(self):
        return 'Descrição da proposta: %s' % (self.proposta)

