'''
Created on Aug 29, 2016

@author: andre
'''

class Position(object):
    '''
    classdocs
    '''


    def __init__(self, _x, _y):
        '''
        Constructor
        '''        
        self.x = _x
        self.y = _y
        
    def copy(self):
        return Position(self.x, self.y)
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        
    def __eq__(self, position):
        if isinstance(position, Position) or isinstance(position, tuple):
            return (position[0] == self[0]) and (position[1] == self[1])
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        else:
            return self.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return repr((self[0], self[1]))
    
    def __add__(self, position):
        x = self.x + position[0]
        y = self.y + position[1]
        return Position(x, y)
    
if __name__ == "__main__":
    p = Position(1, 0)
    print(p * 3)  # != 3*p 
    
