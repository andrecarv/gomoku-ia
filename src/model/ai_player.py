'''
Created on Sep 5, 2016

@author: andre
'''
import sys

SEQUENCE_SCORE = {1: 10, 2:1000, 3:50000, 4:1000000, 5:sys.maxsize}


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, color):
        '''
        Constructor
        '''
        self.color = color
    
    
    def evaluate_board(self, board):
        blocked = False
        double_blocked = False
        total = 0
        for piece in board:
            number_pieces = 1
            # sum pieces with same color in each way (max of four positions on each direction) (left-right, up-down, left top-right bottom, left bottom-right top)
            # if find a piece with different color set blocked to true, if already blocked set double_blocked
            # if double_blocked, continue to next piece
            if double_blocked:
                score = 0
                continue
            # select score according to number of pieces
            score = SEQUENCE_SCORE[number_pieces]
            # if piece.get_color() != ia_color multiply score by -1
            if blocked:
                score / 10
            total += score
        pass