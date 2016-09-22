'''
Created on Sep 20, 2016

@author: andre
'''

class Sequence(object):
    '''
    classdocs
    '''


    def __init__(self, color):
        '''
        Constructor
        '''
        self.set_of_pieces = frozenset()
        self.color = color
        self.bblocked = False
        self.fblocked = False
        
    def add(self, piece):
        aux = [p for p in self.set_of_pieces]
        aux.append(piece)
        self.set_of_pieces = frozenset(aux)
        
    def is_bblocked(self):
        return self.bblocked
    
    def is_fblocked(self):
        return self.fblocked
    
    def get_color(self):
        return self.color
    
    def set_bblocked(self):
        self.bblocked = True
        
    def set_fblocked(self):
        self.fblocked = True
        
    def __eq__(self, pieces):
        return self.set_of_pieces == pieces
        
    def __hash__(self):
        return hash(self.set_of_pieces)
        
    def __len__(self):
        return len(self.set_of_pieces)

if __name__ == '__main__':
    conj = set()
    seq1 = Sequence("red")
    seq2 = Sequence("green")
    s = "string"
    seq1.add(s)
    seq2.add(s)
    conj.add(seq1)
    conj.add(seq2)
    for i in conj:
        print(i)
        
        