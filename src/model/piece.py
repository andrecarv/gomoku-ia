'''
Created on Aug 29, 2016

@author: andre
'''
from model.position import Position

class Piece(object):
    '''
    classdocs
    '''
    
    def __init__(self, position, color):
        '''
        Constructor
        '''
        self.position = position
        self.color = color
        
    def __repr__(self):
        return self.color
        
    def get_position(self):
        return self.position.copy()
    
    def get_color(self):
        return self.color
        
