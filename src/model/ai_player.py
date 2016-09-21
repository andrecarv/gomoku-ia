'''
Created on Sep 5, 2016

@author: andre
'''
import sys
from model.board import Board, DIRECTIONS
from game import PLAYER_COLOR
from model.sequence import Sequence

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
    
    def _get_sequence(self, piece, board, bvect, fvect, index):
        bpos = piece._get_pos()
        color = piece.get_color()
        seq = Sequence(color)
        seq.add(piece)
        aux_index = index
        for i in range(aux_index):
            bpos += bvect
            if board.color_at() == color:
                seq.add(board.piece_at(bpos))
            elif board.color_at() is not None or not board.inbounds(bpos):
                aux_index = i + 1
                seq.set_bblocked()
                break
        fpos = piece._get_pos()
        for i in range(4 - aux_index):
            fpos += fvect
            if board.color_at() == color:
                seq.add(board.piece_at(fpos))
            elif board.color_at() is not None or not board.inbounds(bpos):
                aux_index = (4-aux_index) - i
                seq.set_fblocked()
                if seq.is_bblocked():
                    return seq
                break
        if seq.is_fblocked():
            for i in range(aux_index):
                bpos += bvect
                if board.color_at() == color:
                    seq.add(board.piece_at(bpos))
                elif board.color_at() is not None or not board.inbounds(bpos):
                    aux_index = i + 1
                    seq.set_bblocked()
                    break
        return seq
    
    def evaluate_board(self, board):
        sequences = {PLAYER_COLOR[1]: set(), PLAYER_COLOR[-1]:set()}
        total = 0
        for pos, piece in board.get_pieces().items():
            c = piece.get_color()
            for vectors in DIRECTIONS:
                for i in range(5):
                    seq = self._get_sequence(piece, board, vectors[0], vectors[1], i)
                    if seq.is_bblocked() and seq.is_fblocked():
                        continue
                    sequences[seq.get_color()].add(seq)
                
            # sum pieces with same color in each way (max of four positions on each direction) (left-right, up-down, left top-right bottom, left bottom-right top)
            # if find a piece with different color set blocked to true, if already blocked set double_blocked
            # if double_blocked, continue to next piece
        score = 0
        for seq in sequences[PLAYER_COLOR[1]]:
            if seq.is_bblocked() or seq.is_fblocked():
                score += SEQUENCE_SCORE[len(seq)] / 10
                continue
            score += SEQUENCE_SCORE[len(seq)]
        total = total + score
        score = 0
        for seq in sequences[PLAYER_COLOR[-1]]:
            if seq.is_bblocked() or seq.is_fblocked():
                score += SEQUENCE_SCORE[len(seq)] / 10
                continue
            score += SEQUENCE_SCORE[len(seq)]
        total = total - score
        return total

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
    
    
#                 # first atempt of verifying sequences
#            for vectors in DIRECTIONS:
#                 bseq, fseq = Sequence(c), Sequence(c)
#                 b_empty_spaces, f_empty_spaces = 0, 0
#                 bseq.add(piece), fseq.add(piece)
#                 bpos, fpos = pos, pos
#                 for i in range(4):
#                     bpos += vectors[0]
#                     color = board.color_at(bpos)
#                     if color == c:
#                         bseq.add(board.piece_at(bpos))
#                     elif color is None:
#                         b_empty_spaces += 1
#                     else:
#                         bseq.set_blocked()
#                         break
#                 for i in range(4):
#                     fpos += vectors[1]
#                     color = board.color_at(fpos)
#                     if color == c:
#                         fseq.add(board.piece_at(fpos))
#                     elif color is None:
#                         f_empty_spaces += 1
#                     else:
#                         fseq.set_blocked()
#                         break
#                 # middle
#                 baux = [None, None, None, None, None, None, None]
#                 faux = [None, None, None]
#                 mseq1, mseq2, mseq3 = Sequence(c), Sequence(c), Sequence(c)
#                 aux_pos = vectors[0] * 3 + pos
#                 for i in range(7):    
#                     aux_pos += vectors[1]
#                     aux[i] = board.piece_at(aux_pos)
#                 
#                 [mseq1.add(p) for p in aux[:5] if (p is not None)]
#                 [mseq2.add(p) for p in aux[1:] if (p is not None)]
#                 [mseq3.add(p) for p in aux[2:] if (p is not None)]
#                 if bseq.is_blocked() or fseq.is_blocked(): 
#                     if bseq.is_blocked() and fseq.is_blocked():    
#                         if (len(bseq) + len(fseq) - 1) + (f_empty_spaces + b_empty_spaces) > 4:
#                             for p in fseq:
#                                 bseq.add(p)
#                             sequences[c].add(bseq)
#                             break
#                         else:
#                             break
#                         xoo_o_oox
#                     
#                         pass
#                     else:  # score is divided by ten
#                         if bseq.is_blocked():
#                             fpos = pos
#                             for i in range(5 - len(bseq)):
#                                 fpos += vectors[1]
#                                 if board.color_at(fpos) == c:
#                                     bseq.add(board.piece_at(fpos))
#                         elif fseq.is_blocked():
#                             bpos = pos
#                             for i in range(5 - len(fseq)):
#                                 bpos += vectors[0]
#                                 if board.color_at(bpos) == c:
#                                     bseq.add(board.piece_at(bpos))
#                         
#                             
#                             
#                             pass
#                         pass
#                 
