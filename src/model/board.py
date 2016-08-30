'''
Created on Aug 29, 2016

@author: andre
'''
#    1 2 3
#    4   5
#    6 7 8
DIRECTIONS = [(-1, -1), (0, -1), (1, -1), (-1, 0),
               (1, 0), (-1, 1), (0, 1), (1, 1)]

class Board(object):
    '''
    classdocs
    '''


    def __init__(self, _pieces=None):
        '''
        Constructor
        '''
        self.pieces = {}  # { Key : value } -> { Position : Piece }
        
    def insert_piece(self, piece):
        pos = piece.get_position()
        out_of_bounds = (pos[0] < 0 or pos[0] > 14) or (pos[1] < 0 or pos[1] > 14)
        if pos in self.pieces.keys() or out_of_bounds:
            return False
        self.pieces[pos] = piece
        return True
    
    def piece_at(self, position):
        if position in self.pieces.keys():
            return self.pieces[position]
        else:
            return None
    
    def verify_game_over(self):
        print(self.pieces)
        for pos, piece in self.pieces.items():
            color = piece.get_color()
            for vector in DIRECTIONS:
                if self.verify_sequence(pos, vector, color):
                    return True
        return False
        
    def verify_sequence(self, pos, vector, color):
        sequence = 1
        for i in range(4):
            pos += vector
            if self.piece_at(pos) is None:
                continue
            if self.piece_at(pos).color == color:
                sequence += 1
            if sequence == 5:
                return True
        pass
