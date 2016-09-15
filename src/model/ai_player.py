'''
Created on Sep 5, 2016

@author: andre
'''
import sys
from model.board import Board

SEQUENCE_SCORE = {1: 10, 2:1000, 3:50000, 4:1000000, 5:sys.maxsize}

class AINode(Board):
    
    def __init__(self, board=None, value=None):
        super(Board, self).__init__(board.get_pieces())
        self.last_piece_played = board._get_last_move()
        self.value = value
        
    def set_value(self, value):
        self.value = value
        
    def get_value(self):
        return self.value
    
    def copy(self):
        return AINode(self, self.value)
    
    def __eq__(self, ainode):
        return self.value == ainode.get_value()
    
    def __gt__(self, ainode):
        return self.value > ainode.get_value()
    
    def __ge__(self, ainode):
        return self.value >= ainode.get_value()
    
    def __lt__(self, ainode):
        return self.value < ainode.get_value()
    
    def __le__(self, ainode):
        return self.value <= ainode.get_value()
    
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


class AIPlayer(object):
    '''
    classdocs
    '''

    def __init__(self, color):
        '''
        Constructor
        '''
        self.color = color
        
    def derivate(self, ainode):
        last_color = ainode.get_last_move().get_color()
        color = 'green'
        if last_color is 'green':
            color = 'red'
        children = []
        from model.board import DIRECTIONS
        from model.piece import Piece
        DIRECTIONS
        for base_pos in ainode.get_pieces().keys():
            for vectors in DIRECTIONS:
                pos = base_pos
                for i in range(4):  # @UnusedVariable
                    pos += vectors[0]
                    if ainode.board.piece_at(pos) is None and ainode.inbounds(pos):
                        child = ainode.copy()
                        child.board.put_piece(Piece(pos, color))
                        children.append(child)
                    else:
                        break
                pos = base_pos
                for i in range(4):  # @UnusedVariable
                    pos += vectors[1]
                    if ainode.board.piece_at(pos) is None and ainode.inbounds(pos):
                        child = ainode.copy()
                        child.board.put_piece(Piece(pos, color))
                        children.append(child)
                    else:
                        break
        return children
    
    def minimax(self, ainode, depth=4, alpha=AINode(value=(-sys.maxsize)), beta=AINode(value=(sys.maxsize)),
                maximizingPlayer=True):
        if depth == 0 or ainode.verify_game_over():
            return ainode.evaluate_board()
        if maximizingPlayer:
            best_value = AINode(best_value=(-sys.maxsize))
            for child in self.derivate(ainode):
                best_value = max(best_value, self.minimax(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, child)
                if beta <= alpha:
                    break
            return best_value
        else:
            best_value = AINode(best_value=(sys.maxsize))
            for child in self.derivate(ainode):
                best_value = min(best_value, self.minimax(child, depth - 1, alpha, beta, True))
                alpha = min(beta, best_value)
                if beta <= alpha:
                    break
            return best_value
    
    
