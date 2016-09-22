'''
Created on Sep 5, 2016

@author: andre
'''
import sys
from model.board import Board, DIRECTIONS
from model.sequence import Sequence

SEQUENCE_SCORE = {1: 10, 2:500, 3:10000, 4:500000, 5:sys.maxsize}

class AINode(Board):
    
    def __init__(self, board=None, value=None):
        super(Board, self).__init__()
        if board is not None:
            self.pieces = board.get_pieces()
            self.last_piece_played = board._get_last_move()
        self.moves = []
        self.value = value

    def get_move(self):
        if len(self.moves) > 0:
            return self.moves[0]
        
    def put_piece(self, piece):
        self.moves.append(piece)
        return Board.put_piece(self, piece)
        
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
    
    def _get_sequence(self, piece, bvect, fvect, index):
        bpos = piece.get_position()
        color = piece.get_color()
        seq = Sequence(color)
        seq.add(piece)
        aux_index = index
        for i in range(index):
            bpos += bvect
            if self.color_at(bpos) == color:
                seq.add(self.piece_at(bpos))
            elif self.color_at(bpos) is not None or not self.inbounds(bpos):
                aux_index = i
                seq.set_bblocked()
                break
        fpos = piece.get_position()
        for i in range(4 - aux_index):
            fpos += fvect
            if self.color_at(fpos) == color:
                seq.add(self.piece_at(fpos))
            elif self.color_at(fpos) is not None or not self.inbounds(bpos):
                aux_index = i
                seq.set_fblocked()
                if seq.is_bblocked():
                    return seq
                break
        if seq.is_fblocked():
            for i in range(4 - aux_index):
                bpos += bvect
                if self.color_at(bpos) == color:
                    seq.add(self.piece_at(bpos))
                elif self.color_at(bpos) is not None or not self.inbounds(bpos):
                    seq.set_bblocked()
                    break
        return seq
    
    def evaluate_board(self, ai_color):
#         print("Evaluating...")
        sequences = {ai_color: set()}
        player_color = 'red'
        if ai_color == 'red':
            player_color = 'green'
        sequences[player_color] = set()
        total = 0
        for piece in self.pieces.values():
            for vectors in DIRECTIONS:
                for i in range(5):
                    seq = self._get_sequence(piece, vectors[0], vectors[1], i)
                    if seq.is_bblocked() and seq.is_fblocked():
                        continue
                    sequences[seq.get_color()].add(seq)
        score = 0
        print(("tamanhos ", len(sequences[ai_color]), len(sequences[player_color])))
        for seq in sequences[ai_color]:
            if seq.is_bblocked() or seq.is_fblocked():
                score += SEQUENCE_SCORE[len(seq)] / 10
                continue
            score += SEQUENCE_SCORE[len(seq)]
        total = total + score
        score = 0
        for seq in sequences[player_color]:
            if seq.is_bblocked() or seq.is_fblocked():
                score += SEQUENCE_SCORE[len(seq)] / 10
                continue
            score += SEQUENCE_SCORE[len(seq)]
        total = total - score
        self.value = total
        print('evaluation: ', self.value)

class AIPlayer(object):
    '''
    classdocs
    '''

    def __init__(self, color, difficulty):
        '''
        Constructor
        '''
        self.color = color
        self.difficulty = difficulty
        
    def get_move(self, board):
        return self.minimax(AINode(board), depth=self.difficulty).get_move()
        
    def derivate(self, ainode):
        last_color = ainode._get_last_move().get_color()
        color = 'green'
        if last_color is 'green':
            color = 'red'
        positions = set()
        children = []
        from model.piece import Piece
        for base_pos in ainode.get_pieces().keys():
            for vectors in DIRECTIONS:
                pos = base_pos
                for i in range(2):  # @UnusedVariable
                    pos += vectors[0]
                    if ainode.piece_at(pos) is None and ainode.inbounds(pos):
                        positions.add(pos)
                    else:
                        break
                pos = base_pos
                for i in range(2):  # @UnusedVariable
                    pos += vectors[1]
                    if ainode.piece_at(pos) is None and ainode.inbounds(pos):
                        positions.add(pos)
                    else:
                        break
        for pos in positions:
            child = ainode.copy()
            child.put_piece(Piece(pos, color))
            children.append(child)
        return children
    
    def _max(self, ainode1, ainode2):
        if ainode2 > ainode1:
            return ainode2
        return ainode1
    
    def _min(self, ainode1, ainode2):
        if ainode2 < ainode1:
            return ainode2
        return ainode1
        
    
    def minimax(self, ainode, depth=4, alpha=AINode(value=(-sys.maxsize)), beta=AINode(value=(sys.maxsize)),
                maximizingPlayer=True):
        if depth == 0 or ainode.verify_game_over() == 'end':
            ainode.evaluate_board(self.color)
            return ainode
        if maximizingPlayer:
            best_value = AINode(value=(-sys.maxsize))
            for child in self.derivate(ainode):
                best_value = self._max(best_value, self.minimax(child, depth - 1, alpha, beta, False))
                alpha = self._max(alpha, best_value)
                if beta <= alpha:
                    break
        else:
            best_value = AINode(value=(sys.maxsize))
            for child in self.derivate(ainode):
                best_value = self._min(best_value, self.minimax(child, depth - 1, alpha, beta, True))
                alpha = self._min(beta, best_value)
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
